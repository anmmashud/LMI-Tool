import subprocess
from colorama import Fore, Style, init
init(autoreset=True)

def reboot_to_recovery():
    print(Fore.WHITE + "Rebooting to recovery mode..." + Style.RESET_ALL)
    subprocess.run(["adb", "reboot", "recovery"], check=True)
    print(Fore.GREEN + "Reboot to recovery mode completed." + Style.RESET_ALL)

if __name__ == "__main__":
    reboot_to_recovery()
