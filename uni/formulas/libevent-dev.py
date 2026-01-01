from uni.formula import Formula
from uni.source import Source


class LibeventDev(Formula):
    name = "libevent-dev"
    description = "Development files for the libevent library"
    version = "x.x.x"
    bin = "libevent-dev"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="libevent-dev",
                debian="libevent-dev",
                arch="libevent",
                fedora="libevent-devel",
            ),
        ]

    def test(self):
        return True
