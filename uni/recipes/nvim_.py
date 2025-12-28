from uni.recipe import Recipe


class Nvim(Recipe):
    name = "nvim"
    description = "Vim-fork focused on extensibility and usability"
    version = "0.11.5"
    bin = "bin/nvim"

    sources = {
        "linux-x86_64": {
            "url": "https://github.com/neovim/neovim/releases/download/v0.11.5/nvim-linux-x86_64.tar.gz",
            "sha256": "b2f91117be5b5ea39edd7297156dc2a4a8df4add6c95a90809a8df19e7ab6f52",
        },
        "linux-arm64": {
            "url": "https://github.com/neovim/neovim/releases/download/v0.11.5/nvim-linux-arm64.tar.gz",
            "sha256": "ea4f9a31b11cc1477ff014aebb7b207684e7280f94ffa97abdab6cacd9b98519",
        },
    }

    def post_install(self):
        pass
