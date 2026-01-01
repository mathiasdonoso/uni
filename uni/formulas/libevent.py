from uni.formula import Formula
from uni.source import Source


class Libevent(Formula):
    name = "libevent"
    description = "libevent is a software library that provides asynchronous event notification"
    version = "x.x.x"
    bin = "libevent"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="libevent",
                debian="libevent",
                arch="libevent",
                fedora="libevent",
            ),
        ]

    def test(self):
        return True
