from uni.formula import Formula
from uni.source import Source


class Bison(Formula):
    name = "bison"
    description = "Utility for directing compilation"
    version = "x.x.x"
    bin = "bison"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="bison",
                debian="bison",
                arch="bison",
                fedora="bison",
            ),
        ]

    def test(self):
        return True
