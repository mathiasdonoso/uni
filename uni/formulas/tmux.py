from uni.formula import Formula
from uni.source import Source


class Tmux(Formula):
    name = "tmux"
    description = "tmux is a terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a single screen. tmux may be detached from a screen and continue running in the background, then later reattached."
    version = "3.6a"
    bin = "tmux"

    def sources(self):
        return [
            Source.prebuilt_binary(
                artifacts={
                    "linux-x86_64": {
                        "url": "https://github.com/tmux/tmux-builds/releases/download/v3.6a/tmux-3.6a-linux-x86_64.tar.gz",
                        "sha256": "c0a772a5e6ca8f129b0111d10029a52e02bcbc8352d5a8c0d3de8466a1e59c2e",
                        "bin": ""
                    },
                    "linux-arm64": {
                        "url": "https://github.com/tmux/tmux-builds/releases/download/v3.6a/tmux-3.6a-linux-arm64.tar.gz",
                        "sha256": "bb5afd9d646df54a7d7c66e198aa22c7d293c7453534f1670f7c540534db8b5e",
                        "bin": ""
                    },
                }
            ),
            Source.build_from_source(
                url="https://github.com/tmux/tmux/releases/download/3.6a/tmux-3.6a.tar.gz",
                sha256="b6d8d9c76585db8ef5fa00d4931902fa4b8cbe8166f528f44fc403961a3f3759",
                build_deps=[
                    "make",
                    "gcc",
                    "libevent",
                    "ncurses",
                    "bison",
                    "pkg-config"
                ],
                build_steps=[
                    "./configure",
                    "make",
                    ["make", "install"]
                ],
            ),
        ]
    
    def test(self):
        return True

