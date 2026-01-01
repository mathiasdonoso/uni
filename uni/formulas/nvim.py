from uni.formula import Formula
from uni.source import Source


class Nvim(Formula):
    name = "nvim"
    description = "Vim-fork focused on extensibility and usability"
    version = "0.11.5"
    bin = "bin/nvim"

    def sources(self):
        return [
            Source.prebuilt_binary(
                artifacts={
                    "linux-x86_64": {
                        "url": "https://github.com/neovim/neovim/releases/download/v0.11.5/nvim-linux-x86_64.tar.gz",
                        "sha256": "b2f91117be5b5ea39edd7297156dc2a4a8df4add6c95a90809a8df19e7ab6f52",
                        "bin": "bin/nvim"
                    },
                    "linux-arm64": {
                        "url": "https://github.com/neovim/neovim/releases/download/v0.11.5/nvim-linux-arm64.tar.gz",
                        "sha256": "ea4f9a31b11cc1477ff014aebb7b207684e7280f94ffa97abdab6cacd9b98519",
                        "bin": "bin/nvim"
                    },
                }
            ),
            Source.build_from_source(
                url="https://github.com/neovim/neovim/archive/refs/tags/v0.11.5.tar.gz",
                sha256="c63450dfb42bb0115cd5e959f81c77989e1c8fd020d5e3f1e6d897154ce8b771",
                build_deps=["make"],
                build_steps=[
                    "make CMAKE_BUILD_TYPE=Release",
                    "make install",
                ],
            ),
        ]
    
    def test(self):
        return True

