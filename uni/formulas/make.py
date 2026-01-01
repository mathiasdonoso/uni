from uni.formula import Formula
from uni.source import Source


class Make(Formula):
    name = "make"
    description = "Utility for directing compilation"
    version = "4.4.1"
    bin = "tmux"

    def sources(self):
        return [
            # Source.build_from_source(
            #     url="https://ftp.gnu.org/gnu/make/make-4.4.1.tar.lz",
            #     sha256="8814ba072182b605d156d7589c19a43b89fc58ea479b9355146160946f8cf6e9",
            #     build_deps=["make"],
            #     build_steps=[
            #         "./configure",
            #         "make install",
            #     ],
            # ),
            Source.package_manager(
                ubuntu="make",
                debian="make",
                arch="make",
                fedora="make",
            ),
        ]

    def test(self):
        return True
