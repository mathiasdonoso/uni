from uni.formula import Formula
from uni.source import Source


class Stow(Formula):
    name = "stow"
    description = "GNU stow is a symlink farm manager which takes distinct packages of software and/or data located in separate directories on the filesystem, and makes them appear to be installed in the same place"
    version = "x.x.x"
    bin = "stow"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="stow",
                debian="stow",
                arch="stow",
                fedora="stow",
            ),
        ]

    def test(self):
        return True
