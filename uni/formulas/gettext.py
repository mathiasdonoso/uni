from uni.formula import Formula
from uni.source import Source


class GetText(Formula):
    name = "gettext"
    description = "GNU internationalization library"
    version = "x.x.x"
    bin = "gettext"

    def sources(self):
        return [
            Source.package_manager(
                ubuntu="gettext",
                debian="gettext",
                # TODO: gettext is already in the arch core package, maybe ignore it for arch?
                arch="gettext",
                fedora="gettext",
            ),
        ]

    def test(self):
        return True
