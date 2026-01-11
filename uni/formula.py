class Formula:
    name = None
    description = None
    version = None

    def sources(self):
        """
        Return list of Source objects in priority order.
        Override this method in subclasses.
        """
        raise NotImplementedError("Subclass must implement sources()")

    def test(self) -> bool:
        """
        Optional: Test that installation worked.
        Return True if test passes, False otherwise.
        """
        return True

    def package_manager_post_install(self) -> bool:
        """
        Optional: post-installation steps only when installing via a package manager.
        Return True if all steps complete successfully; otherwise, return False.
        """
        return True
