from uni.formula import Formula
from uni.source import Source


class Ninja(Formula):
    name = "ninja"
    description = "Build system"
    version = "x.x.x"
    bin = "ninja"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="ninja-build",
                debian="ninja-build",
                arch="ninja",
                fedora="ninja-build",
            ),
        ]

    def test(self):
        return True
