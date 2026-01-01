from uni.formula import Formula
from uni.source import Source


class GCC(Formula):
    name = "c-compiler"
    description = "C Compiler"
    version = "x.x.x"
    bin = "gcc"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="build-essential",
                debian="build-essential",
                arch="gcc",
                fedora="gcc",
            ),
        ]

    def test(self):
        return True
