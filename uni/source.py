class Source:
    """Base class for package sources"""
    
    def __init__(self, source_type, **kwargs):
        self.type = source_type
        self.config = kwargs
    
    @classmethod
    def prebuilt_binary(cls, artifacts):
        """Direct binary download (not from GitHub)"""
        return cls("prebuilt_binary", artifacts=artifacts)

    @classmethod
    def package_manager(cls, **distro_packages):
        """Use system package manager"""
        return cls("package_manager", packages=distro_packages)
    
    @classmethod
    def build_from_source(cls, url, sha256, build_deps=None, runtime_deps=None, build_steps=None):
        """Build from source tarball"""
        return cls(
            "build_from_source",
            url=url,
            sha256=sha256,
            build_deps=build_deps or [],
            runtime_deps=runtime_deps or [],
            build_steps=build_steps or []
        )
