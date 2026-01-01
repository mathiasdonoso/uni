from uni.formula import Formula
from uni.source import Source


class Fzf(Formula):
    name = "fzf"
    description = "general-purpose command-line fuzzy finder"
    version = "0.67.0"
    bin = "fzf"

    def sources(self):
        return [
            Source.prebuilt_binary(
                artifacts={
                    "linux-x86_64": {
                        "url": "https://github.com/junegunn/fzf/releases/download/v0.67.0/fzf-0.67.0-linux_amd64.tar.gz",
                        "sha256": "4be08018ca37b32518c608741933ea335a406de3558242b60619e98f25be2be1",
                        "bin": ""
                    },
                    "linux-arm64": {
                        "url": "https://github.com/junegunn/fzf/releases/download/v0.67.0/fzf-0.67.0-linux_arm64.tar.gz",
                        "sha256": "7071f48c2ac0f2bc992d6d33cc36fd675a579a98cc976dda699eea07dd5e9c58",
                        "bin": ""
                    },
                }
            ),
            Source.package_manager(
                ubuntu="fzf",
                debian="fzf",
                arch="fzf",
                fedora="fzf",
            ),
        ]
    
    def test(self):
        return True

