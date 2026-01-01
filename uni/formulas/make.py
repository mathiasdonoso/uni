from uni.formula import Formula
from uni.source import Source


class Make(Formula):
    name = "make"
    description = "Utility for directing compilation"
    version = "4.4.1"
    bin = "make"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="make",
                debian="make",
                arch="make",
                fedora="make",
            ),
        ]

    def test(self):
        return True
