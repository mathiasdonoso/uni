from uni.formula import Formula
from uni.source import Source


class Tmux(Formula):
    name = "tmux"
    description = "tmux is a terminal multiplexer: it enables a number of terminals to be created, accessed, and controlled from a single screen. tmux may be detached from a screen and continue running in the background, then later reattached."
    version = "3.6a"
    bin = "tmux"

    def sources(self):
        return [
            Source.build_from_source(
                url="https://github.com/tmux/tmux/releases/download/3.6a/tmux-3.6a.tar.gz",
                sha256="b6d8d9c76585db8ef5fa00d4931902fa4b8cbe8166f528f44fc403961a3f3759",
                build_deps=["make"],
                build_steps=[
                    "./configure",
                    "make",
                ],
            ),
        ]
    
    def validate(self):
        pass

