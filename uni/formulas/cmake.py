from uni.formula import Formula
from uni.source import Source


class CMake(Formula):
    name = "cmake"
    description = "Utility for directing compilation"
    version = "x.x.x"
    bin = "cmake"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="cmake",
                debian="cmake",
                arch="cmake",
                fedora="cmake",
            ),
        ]

    def test(self):
        return True
