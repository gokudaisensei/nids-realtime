import os
import subprocess
import sys
import platform


def is_windows():
    return platform.system() == "Windows"


def is_npcap_installed():
    try:
        subprocess.check_output("npcap --version", shell=True)
        return True
    except subprocess.CalledProcessError:
        return False


def install_npcap():
    # Download the Npcap installer (adjust the URL if needed)
    npcaps_installer_url = "https://npcap.com/dist/npcap-1.77.exe"
    installer_filename = "NpcapInstaller.exe"
    os.system(f"curl -o {installer_filename} {npcaps_installer_url}")

    # Run the installer silently
    os.system(f"{installer_filename} /S")

    # Clean up the installer file
    os.remove(installer_filename)


def main():
    if is_windows():
        if is_npcap_installed():
            print("Npcap is already installed.")
        else:
            print("Npcap is not installed. Installing...")
            install_npcap()
            print("Npcap has been installed.")
    else:
        print("This script is intended for Windows systems only.")
        sys.exit(1)


if __name__ == "__main__":
    main()
