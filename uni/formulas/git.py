from uni.formula import Formula
from uni.source import Source


class Git(Formula):
    name = "git"
    description = "Git is a distributed version control software system that is capable of managing versions of source code or data"
    version = "x.x.x"
    bin = "git"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="git",
                debian="git",
                arch="git",
                fedora="git",
            ),
        ]

    def test(self):
        return True
