from uni.recipe import Recipe


class Tmux(Recipe):
    name = "tmux"
    description = "tmux is a terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a single screen. tmux may be detached from a screen and continue running in the background, then later reattached."
    version = "3.6a"
    bin = "rg"

    sources = {
        "universal": {
            "url": "https://github.com/tmux/tmux/releases/download/3.6a/tmux-3.6a.tar.gz",
            "sha256": "sha256:b6d8d9c76585db8ef5fa00d4931902fa4b8cbe8166f528f44fc403961a3f3759",
        },
    }

    def post_install(self):
        pass

