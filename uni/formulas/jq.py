from uni.formula import Formula
from uni.source import Source


class Jq(Formula):
    name = "jq"
    description = "Command-line JSON processor"
    version = "1.8.1"
    bin = "jq"

    def sources(self):
        return [
            Source.prebuilt_binary(
                artifacts={
                    "linux-x86_64": {
                        "url": "https://github.com/jqlang/jq/releases/download/jq-1.8.1/jq-linux-amd64",
                        "sha256": "020468de7539ce70ef1bceaf7cde2e8c4f2ca6c3afb84642aabc5c97d9fc2a0d",
                        "bin": "jq"
                    },
                    "linux-arm64": {
                        "url": "https://github.com/jqlang/jq/releases/download/jq-1.8.1/jq-linux-arm64",
                        "sha256": "6bc62f25981328edd3cfcfe6fe51b073f2d7e7710d7ef7fcdac28d4e384fc3d4",
                        "bin": "jq"
                    },
                }
            ),
        ]
    
    def test(self):
        return True

