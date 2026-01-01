from uni.formula import Formula
from uni.source import Source


class NCurses(Formula):
    name = "ncurses"
    description = "ncurses is a programming library for creating textual user interfaces that work across a wide variety of terminals"
    version = "x.x.x"
    bin = "ncurses"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="ncurses",
                debian="ncurses",
                arch="ncurses",
                fedora="ncurses",
            ),
        ]

    def test(self):
        return True
