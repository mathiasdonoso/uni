from uni.formula import Formula
from uni.source import Source


class Curl(Formula):
    name = "curl"
    description = "cURL is a computer software project providing a library and command-line tool for transferring data using various network protocols"
    version = "x.x.x"
    bin = "curl"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="curl",
                debian="curl",
                arch="curl",
                fedora="curl",
            ),
        ]

    def test(self):
        return True
