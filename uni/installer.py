import platform
import hashlib
import tarfile
import tempfile
import subprocess
from pathlib import Path
from urllib.request import urlretrieve


OPT_BASE = Path("/opt/uni")

class Installer:
    def __init__(self):
        self.install_dir = Path.home() / ".local" / "bin"
        self.install_dir.mkdir(parents=True, exist_ok=True)
    
    def install(self, formula):
        """Try each source until one succeeds"""
        sources = formula.sources()
        
        for source in sources:
            try:
                if source.type == "prebuilt_binary":
                    print(f"Preparing to install from prebuilt binary")
                    if self._install_prebuilt_binary(source):
                        print(f"Installed {formula.name} from prebuilt binary")
                        return True
                elif source.type == "build_from_source":
                    print(f"Preparing to install from source")
                    if self._install_build_from_source(source):
                        print(f"Built and installed {formula.name} from source")
                        return True
            
            except Exception as e:
                print(f"Failed: {e}")
                continue
        
        raise Exception(f"All installation methods failed for {formula.name}")
    
    def _install_prebuilt_binary(self, source):
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
    
            print(f"Downloading from {url}...")
            archive = tmpdir / "archive.tar.gz"
            urlretrieve(url, archive)
    
            if not self._verify_checksum(archive, expected_sha256):
                raise Exception("Checksum verification failed")
    
            extract_dir = tmpdir / "extract"
            extract_dir.mkdir()

            with tarfile.open(archive, "r:gz") as tar:
                tar.extractall(extract_dir)

            extracted_root = next(
                p for p in extract_dir.iterdir() if p.is_dir()
            )
    
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
    
    def _install_package_manager(self, source):
        """Use system package manager"""
        distro = self._detect_distro()
        print(f"distro: %s", distro)
        return
        
        packages = source.config.get("packages", {})
        
        if distro not in packages:
            raise Exception(f"No package mapping for {distro}")
        
        package_name = packages[distro]
        
        # Detect package manager and install
        if distro in ["debian", "ubuntu"]:
            cmd = ["sudo", "apt", "install", "-y", package_name]
        elif distro == "arch":
            cmd = ["sudo", "pacman", "-S", "--noconfirm", package_name]
        elif distro in ["fedora", "rhel"]:
            cmd = ["sudo", "dnf", "install", "-y", package_name]
        else:
            raise Exception(f"Unsupported distro: {distro}")
        
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            raise Exception(f"Package manager failed: {result.stderr}")
        
        return True
    
    def _install_build_from_source(self, source):
        """Build from source - not implemented yet"""
        raise Exception("Build from source not implemented in v1")
    
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
