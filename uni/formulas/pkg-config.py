from uni.formula import Formula
from uni.source import Source


class PkgConfig(Formula):
    name = "pkg-config"
    description = "pkg-config is software development tool that queries information about libraries from a local, file-based database for the purpose of bulding a codebase that depends on them"
    version = "x.x.x"
    bin = "pkg-config"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="pkg-config",
                debian="pkg-config",
                arch="pkg-config",
                fedora="pkg-config",
            ),
        ]

    def test(self):
        return True
