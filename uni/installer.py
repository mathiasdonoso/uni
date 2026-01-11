import hashlib
import os
import stat
import platform
import subprocess
import tarfile
import tempfile
from pathlib import Path
from urllib.request import urlretrieve
from uni.formula import Formula
from uni.loader import load_formula
from uni.source import Source


# https://en.wikipedia.org/wiki/Executable_and_Linkable_Format#ELF_header
ELF_MAGIC = b"\x7fELF"
OPT_BASE = Path("/opt/uni")


# TODO: move these functions into a utils module?
def is_intended_executable(path: str) -> bool:
    if not os.path.isfile(path):
        return False

    try:
        with open(path, "rb") as f:
            first4 = f.read(4)
            if first4 == ELF_MAGIC:
                return True

            f.seek(0)
            first_line = f.readline(128)
            if first_line.startswith(b"#!"):
                return True
    except OSError:
        return False

    return False


def make_executable(path: str) -> None:
    st = os.stat(path)
    os.chmod(path, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


class Installer:
    def __init__(self):
        self.install_dir = Path.home() / ".local" / "bin"
        self.install_dir.mkdir(parents=True, exist_ok=True)

    def install(self, formula: Formula):
        """Try each source until one succeeds"""
        sources = formula.sources()

        for source in sources:
            try:
                if source.type == "prebuilt_binary":
                    print("Preparing to install from prebuilt binary")
                    if self._install_prebuilt_binary(source):
                        print(f"Installed {formula.name} from prebuilt binary")
                        return True
                elif source.type == "build_from_source":
                    print("Preparing to install from source")
                    if self._install_build_from_source(source):
                        print(f"Built and installed {formula.name} from source")
                        return True
                elif source.type == "package_manager":
                    print("Preparing to install using the package manager")
                    if self._install_package_manager(source):
                        print(f"Installed {formula.name} from the package manager")
                        return formula.package_manager_post_install()

            except Exception as e:
                print(f"Failed: {e}")
                continue

        raise Exception(f"All installation methods failed for {formula.name}")

    def _install_prebuilt_binary(self, source: Source):
        """Download binary from repository releases"""
        system = platform.system().lower()
        machine = platform.machine().lower()

        if machine == "aarch64":
            machine = "arm64"

        platform_key = f"{system}-{machine}"

        if platform_key not in source.config["artifacts"]:
            raise Exception(f"No binary for {platform_key}")

        artifact = source.config["artifacts"][platform_key]
        url = artifact["url"]
        expected_sha256 = artifact["sha256"]
        bin_path = artifact.get("bin", "")

        with tempfile.TemporaryDirectory(prefix="uni-") as tmpdir:
            tmpdir = Path(tmpdir)

            print(f"Downloading binary from {url}...")
            archive = tmpdir / "archive.tar.gz"
            urlretrieve(url, archive)

            if not self._verify_checksum(archive, expected_sha256):
                raise Exception("Checksum verification failed")

            extract_dir = tmpdir / "extract"
            extract_dir.mkdir()
            binary_source = Path()

            if os.path.isfile(archive):
                print("downloaded file is the binary")
                # field `bin` must be defined in the source
                # TODO: how do I make sure the field `bin` is not empty?
                archive = archive.rename(Path(tmpdir) / bin_path)

                if is_intended_executable(str(archive)):
                    make_executable(str(archive))
                    binary_source = archive
            else:
                with tarfile.open(archive, "r:gz") as tar:
                    tar.extractall(extract_dir)

                entries = list(extract_dir.iterdir())
                dirs = [p for p in entries if p.is_dir()]
                files = [p for p in entries if p.is_file()]

                extracted_root = None
                if len(dirs) == 1 and not files:
                    extracted_root = dirs[0]
                elif len(files) == 1 and not dirs:
                    extracted_root = files[0]
                binary_source = extracted_root / bin_path

            if not binary_source.exists():
                raise Exception(f"Binary not found at {binary_source}")

            binary_name = Path(bin_path).name
            binary_dest = self.install_dir / binary_name

            print(f"Installing {binary_name} to {binary_dest}")

            import shutil

            shutil.copy2(binary_source, binary_dest)
            binary_dest.chmod(0o755)

        return True

    def _install_package_manager(self, source: Source):
        """Use system package manager"""
        distro = self._detect_distro()
        packages = source.config.get("packages", {})

        # TODO
        if distro not in packages:
            raise Exception(f"No package mapping for {distro}")

        package_name = packages[distro]
        packages = package_name.split(" ")

        is_root = os.geteuid() == 0

        DISTRO_CMDS = {
            "debian": ["apt", "install", "-y"],
            "ubuntu": ["apt", "install", "-y"],
            "arch": ["pacman", "-S", "--noconfirm"],
            "fedora": ["dnf", "install", "-y"],
            "rhel": ["dnf", "install", "-y"],
        }

        if distro not in DISTRO_CMDS:
            raise ValueError(f"Unsupported distro: {distro}")

        cmd = DISTRO_CMDS[distro] + list(packages)

        if not is_root:
            cmd.insert(0, "sudo")

        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, text=True)

        if result.returncode != 0:
            raise Exception(f"Package manager failed: {result.stderr}")

        return True

    def _install_build_from_source(self, source: Source):
        """Build from source"""
        for dep in source.config["build_deps"]:
            # TODO: Keep an eye on this
            try:
                dep_formula = load_formula(dep)
                self.install(dep_formula)
            except Exception as e:
                print(f"Failed to dependency {dep}: {e}")

        url = source.config["url"]
        expected_sha256 = source.config["sha256"]

        # download source code and running commands
        with tempfile.TemporaryDirectory(prefix="uni-") as tmpdir:
            try:
                tmpdir = Path(tmpdir)

                print(f"Downloading source code from {url}...")
                archive = tmpdir / "code.tar.gz"
                urlretrieve(url, archive)

                if not self._verify_checksum(archive, expected_sha256):
                    raise Exception("Checksum verification failed")

                extract_dir = tmpdir / "extract"
                extract_dir.mkdir()

                with tarfile.open(archive, "r:*") as tar:
                    tar.extractall(extract_dir)

                extracted_root = next(p for p in extract_dir.iterdir() if p.is_dir())

                for cmd in source.config["build_steps"]:
                    result = subprocess.run(cmd, cwd=extracted_root, text=True)

                    if result.returncode != 0:
                        raise Exception(f"command {cmd} failed: {result.stderr}")
            except Exception as e:
                print(f"error downloading source and running it: {e}")

        return True

    def _verify_checksum(self, filepath, expected_sha256):
        """Verify SHA256 checksum"""
        sha256_hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)

        actual = sha256_hash.hexdigest()
        return actual == expected_sha256

    def _detect_distro(self):
        """Detect Linux distribution"""
        try:
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("ID="):
                        distro = line.split("=")[1].strip().strip('"')
                        return distro
        except FileNotFoundError:
            pass

        raise Exception("Could not detect distribution")
