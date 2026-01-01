from uni.formula import Formula
from uni.source import Source


class NCursesDev(Formula):
    name = "ncurses-dev"
    description = "Development files for the ncurses library"
    version = "x.x.x"
    bin = "ncurses-dev"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="ncurses-dev",
                debian="ncurses-dev",
                arch="ncurses",
                fedora="ncurses-devel",
            ),
        ]

    def test(self):
        return True
