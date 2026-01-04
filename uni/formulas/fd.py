from uni.formula import Formula
from uni.source import Source


class Fd(Formula):
    name = "fd"
    description = "A simple, fast and user-friendly alternative to 'find'"
    version = "10.3.0"
    bin = "fd"

    def sources(self):
        return [
            Source.prebuilt_binary(
                artifacts={
                    "linux-x86_64": {
                        "url": "https://github.com/sharkdp/fd/releases/download/v10.3.0/fd-v10.3.0-x86_64-unknown-linux-gnu.tar.gz",
                        "sha256": "c3c2bc79f838e780173fc8f18b337ec273e7ba17c7ff8f551be29fc3c19b7916",
                        "bin": "fd"
                    },
                    "linux-arm64": {
                        "url": "https://github.com/sharkdp/fd/releases/download/v10.3.0/fd-v10.3.0-aarch64-unknown-linux-gnu.tar.gz",
                        "sha256": "66f297e404400a3358e9a0c0b2f3f4725956e7e4435427a9ae56e22adbe73a68",
                        "bin": "fd"
                    },
                }
            ),
            # TODO: Add installation from source: needs rust
            Source.package_manager(
                ubuntu="fd-find",
                debian="fd-find",
                arch="fd",
                fedora="fd-find",
            ),
        ]

    def package_manager_post_install(self):
        print("package_manager_post_install trying to run the ln stuff")
        # TODO: refactor to post_install and filter by source maybe
        # TODO: Do this only for debian/ubuntu based distros
        import shutil
        import subprocess
        from pathlib import Path

        fdfind_path = shutil.which("fdfind")
        if fdfind_path is None:
            return True # not a debian/ubuntu based distro

        try:
            target = Path.home() / ".local/bin/fd"

            result = subprocess.run(
                ["ln", "-sf", fdfind_path, str(target)],
                text=True,
                check=False,
            )

            return result.returncode == 0
        except subprocess.CalledProcessError:
            return False

    def test(self):
        return True

