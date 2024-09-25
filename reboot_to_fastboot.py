import subprocess
from colorama import Fore, Style

def reboot_to_fastboot():
    try:
        print(Fore.WHITE + "Rebooting to fastboot mode..." + Style.RESET_ALL)
        result = subprocess.run(["adb", "reboot", "bootloader"], capture_output=True, text=True)
        if result.returncode == 0:
            print(Fore.GREEN + "Device entered fastboot mode successfully." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Failed to send fastboot command." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)

if __name__ == "__main__":
    reboot_to_fastboot()
