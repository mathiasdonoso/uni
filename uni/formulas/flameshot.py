from uni.formula import Formula
from uni.source import Source


class Flameshot(Formula):
    name = "flameshot"
    description = "Powerful yet simple to use screenshot software"
    version = "x.x.x"
    bin = "flameshot"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="flameshot",
                debian="flameshot",
                arch="flameshot",
                # TODO: Handle installation per distribution
                # `dnf install` works on Fedora but not on AlmaLinux
                fedora="flameshot",
            ),
        ]
    
    def test(self):
        return True

