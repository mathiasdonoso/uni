from uni.formula import Formula
from uni.source import Source


class Ripgrep(Formula):
    name = "ripgrep"
    description = "ripgrep recursively searches directories for a regex pattern while respecting your gitignore"
    version = "15.1.0"
    bin = "rg"

    def sources(self):
        return [
            Source.prebuilt_binary(
                artifacts={
                    "linux-x86_64": {
                        "url": "https://github.com/BurntSushi/ripgrep/releases/download/15.1.0/ripgrep-15.1.0-x86_64-unknown-linux-musl.tar.gz",
                        "sha256": "1c9297be4a084eea7ecaedf93eb03d058d6faae29bbc57ecdaf5063921491599",
                    },
                    "linux-arm64": {
                        "url": "https://github.com/BurntSushi/ripgrep/releases/download/15.1.0/ripgrep-15.1.0-aarch64-unknown-linux-gnu.tar.gz.sha256",
                        "sha256": "adc090417ac10b04f0461742c08dcc25abee4a0ff567fa4692b3a7971fe089ec",
                    },
                }
            ),
        ]
    
    def validate(self):
        pass

