class Formula:
    name = None
    description = None
    homepage = None
    license = None
    version = None
    
    def sources(self):
        """
        Return list of Source objects in priority order.
        Override this method in subclasses.
        """
        raise NotImplementedError("Subclass must implement sources()")
    
    def test(self):
        """
        Optional: Test that installation worked.
        Return True if test passes, False otherwise.
        """
        return True
    
    def run_command(self, cmd):
        """Helper to run shell commands"""
        import subprocess
        try:
            result = subprocess.run(
                cmd,
                check=True,
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except subprocess.CalledProcessError:
            return False
