from uni.formula import Formula
from uni.source import Source


class Libx11Utils(Formula):
    name = "libx11"
    description = ""
    version = "x.x.x"
    bin = "libx11"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="libx11-dev libimlib2-dev libxt-dev",
                debian="libx11-dev libimlib2-dev libxt-dev",
                arch="libx11 imlib2 libxt",
                fedora="libX11-devel imlib2-devel libXt-devel",
            ),
        ]

    def test(self):
        return True
