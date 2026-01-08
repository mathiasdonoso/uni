import sys
from uni.installer import Installer
from uni.loader import load_formula


def cmd_install(packages):
    """Install one or more packages"""
    installer = Installer()
    
    for package in packages:
        print(f"\n==> Installing {package}...")
        try:
            formula = load_formula(package)
            installer.install(formula)
        except Exception as e:
            print(f"Failed to install {package}: {e}")
            sys.exit(1)


def cmd_list():
    """List installed packages"""
    print("List command not implemented yet")
    # TODO: Read from state file and show installed packages


def cmd_update(packages):
    """Update packages"""
    print("Update command not implemented yet")
    # TODO: Check for newer versions and reinstall


def cmd_remove(packages):
    """Remove packages"""
    print("Remove command not implemented yet")
    # TODO: Remove binaries from ~/.local/bin


def cmd_info(package):
    """Show package information"""
    try:
        formula = load_formula(package)
        print(f"Name: {formula.name}")
        print(f"Description: {formula.description}")
        print("\nAvailable sources:")
        for i, source in enumerate(formula.sources(), 1):
            print(f"  {i}. {source.type}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def print_usage():
    """Print help message"""
    print("""uni - Personal package installer for Linux

Usage:
    uni <package>...              Install packages (default action)
    uni install <package>...      Install packages explicitly
    uni update [package]...       Update packages
    uni remove <package>...       Remove packages
    uni list                      List installed packages
    uni info <package>            Show package information
    uni --help, -h                Show this help

Examples:
    uni nvim                    Install nvim
    uni nvim tmux ripgrep       Install multiple packages
    uni info nvim               Show nvim information
    uni update nvim             Update nvim
""")


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    args = sys.argv[1:]
    command = args[0]
    
    if command in ["--help", "-h", "help"]:
        print_usage()
        return
    
    if command == "install":
        if len(args) < 2:
            print("Error: No packages specified")
            sys.exit(1)
        cmd_install(args[1:])
    elif command == "list":
        cmd_list()
    elif command == "update":
        if len(args) < 2:
            print("Error: No packages specified")
            sys.exit(1)
        cmd_update(args[1:])
    elif command == "remove":
        if len(args) < 2:
            print("Error: No packages specified")
            sys.exit(1)
        cmd_remove(args[1:])
    elif command == "info":
        if len(args) < 2:
            print("Error: No package specified")
            sys.exit(1)
        cmd_info(args[1])
    else:
        cmd_install(args)


if __name__ == "__main__":
    main()
