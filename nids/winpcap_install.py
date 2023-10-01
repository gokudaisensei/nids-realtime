import os
import subprocess
import sys
import platform


def is_windows():
    return platform.system() == "Windows"


def is_winpcap_installed():
    try:
        subprocess.check_output("rpcapd.exe --version", shell=True)
        return True
    except subprocess.CalledProcessError:
        return False


def install_winpcap():
    # Download the WinPcap installer (adjust the URL if needed)
    winpcap_installer_url = "https://www.winpcap.org/install/bin/WinPcap_4_1_3.exe"
    installer_filename = "WinPcapInstaller.exe"
    os.system(f"curl -o {installer_filename} {winpcap_installer_url}")

    # Run the installer silently
    os.system(f"{installer_filename} /S")

    # Clean up the installer file
    os.remove(installer_filename)


def main():
    if is_windows():
        if is_winpcap_installed():
            print("WinPcap is already installed.")
        else:
            print("WinPcap is not installed. Installing...")
            install_winpcap()
            print("WinPcap has been installed.")
    else:
        print("This script is intended for Windows systems only.")
        sys.exit(1)
