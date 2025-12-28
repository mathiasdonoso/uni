import hashlib
import os
import platform
import shutil
import tarfile
import tempfile
from pathlib import Path
from urllib.request import urlretrieve


class Recipe:
    name: str = ""
    version: str = ""
    bin: str = ""
    sources: dict = {}

    OPT_BASE = Path("/opt/uni")
    BIN_DIR = Path("/usr/local/bin")

    def install(self):
        self._validate_recipe()
        self._install_binary()

    def _validate_recipe(self):
        missing = [
            field for field in ("name", "version", "bin", "sources")
            if getattr(self, field) is None
        ]
        if missing:
            raise RuntimeError(
                f"invalid recipe {self.__class__.__name__}, "
                f"missing: {', '.join(missing)}"
            )

    def _platform_key(self) -> str:
        arch = platform.machine()

        if arch == "x86_64":
            return "linux-x86_64"
        if arch in ("aarch64", "arm64"):
            return "linux-arm64"

        raise RuntimeError(f"unsupported architecture: {arch}")

    def _sha256sum(self, path: Path) -> str:
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()

    def _install_binary(self):
        key = self._platform_key()

        if key not in self.sources:
            raise RuntimeError(
                f"{self.name} has no source for {key}"
            )

        source = self.sources[key]
        url = source["url"]
        expected_hash = source["sha256"]

        opt_dir = self.OPT_BASE / self.name
        symlink_path = self.BIN_DIR / self.bin

        with tempfile.TemporaryDirectory(prefix="uni-") as tmp:
            tmp = Path(tmp)
            archive = tmp / "archive.tar.gz"
            extract_dir = tmp / "extract"

            urlretrieve(url, archive)

            actual = self._sha256sum(archive)
            if actual != expected_hash:
                raise RuntimeError(
                    f"sha256 mismatch for {self.name}: "
                    f"expected {expected_hash}, got {actual}"
                )

            extract_dir.mkdir()
            with tarfile.open(archive, "r:gz") as tar:
                tar.extractall(extract_dir)

            extracted_root = next(
                p for p in extract_dir.iterdir() if p.is_dir()
            )

            try:
                self.OPT_BASE.mkdir(parents=True, exist_ok=True)
            except PermissionError:
                raise RuntimeError(
                    "permission denied: cannot write to /opt/uni "
                    "(run as root)"
                )

            # replace existing install
            if opt_dir.exists():
                shutil.rmtree(opt_dir)

            shutil.move(str(extracted_root), opt_dir)

        # validate binary
        binary_path = opt_dir / self.bin
        if not binary_path.exists():
            raise RuntimeError(
                f"binary not found at {binary_path}"
            )

        if not os.access(binary_path, os.X_OK):
            raise RuntimeError(
                f"binary is not executable: {binary_path}"
            )

        # symlink in /usr/local/bin
        if symlink_path.exists() or symlink_path.is_symlink():
            symlink_path.unlink()

        os.symlink(binary_path, symlink_path)
