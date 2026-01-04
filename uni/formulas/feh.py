from uni.formula import Formula
from uni.source import Source


class Feh(Formula):
    name = "nvim"
    description = "feh is a light-weight, configurable and versatile image viewer"
    version = "3.11.2"
    bin = "feh"

    def sources(self):
        return [
            Source.build_from_source(
                url="https://feh.finalrewind.org/feh-3.11.2.tar.bz2",
                sha256="020f8bce84c709333dcc6ec5fff36313782e0b50662754947c6585d922a7a7b2",
                build_deps=[
                    "libx11-utils",
                    "gcc",
                ],
                build_steps=[
                    ["make", "xinerama=0", "curl=0"],
                    ["make", "install"],
                ],
            ),
        ]
    
    def test(self):
        return True

