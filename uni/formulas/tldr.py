from uni.formula import Formula
from uni.source import Source


class Tldr(Formula):
    name = "tldr"
    description = "The tldr-pages project is a collection of community-maintained help pages for command-line tools, that aims to be a simpler, more approachable complement to traditional man pages"
    version = "x.x.x"
    bin = "tldr"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="tldr",
                debian="tldr",
                arch="tldr",
                fedora="tldr",
            ),
        ]

    def test(self):
        return True
