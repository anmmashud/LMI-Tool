import os
import subprocess
from colorama import Fore, Style


import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def type_out(text, delay=0.1):
    """Simulates typing effect for the text."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

tool_name = "LMI-Tool"
version = "1.0"
logo = f"""
{Fore.CYAN}||===================================||
          {Fore.GREEN}LMI - Tool {Style.RESET_ALL}  {Fore.YELLOW}v-{version}        {Style.RESET_ALL}
_______________________________________
 {Fore.MAGENTA}Copyright © 2024 SPYRooX{Style.RESET_ALL} {Fore.BLUE}by anmmashud {Style.RESET_ALL}
"""

def display_logo():
    """Displays the logo with a typing effect."""
    print(Fore.CYAN + logo)
    type_out("Welcome to LMI-Tool - Loading...", 0.1)

'''=========================== logo, copyright, version ============================'''

def get_device_status():
    try:
        # Check Fastboot connection
        fastboot_devices = subprocess.run(["fastboot", "devices"], capture_output=True, text=True)
        fastboot_lines = fastboot_devices.stdout.strip().split("\n")
        if len(fastboot_lines) > 0 and fastboot_lines[0]:
            fastboot_model = fastboot_lines[0].split()[1]
            return f"Device: {fastboot_model}\nConnected via Fastboot", "fastboot"

        # Check ADB connection
        adb_devices = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        adb_lines = adb_devices.stdout.strip().split("\n")
        if len(adb_lines) > 1 and "device" in adb_lines[1]:
            adb_model = subprocess.run(["adb", "shell", "getprop", "ro.product.model"], capture_output=True, text=True).stdout.strip()
            return f"Device: {adb_model}\nConnected via ADB", "adb"

        return "No device connected", None
    except Exception as e:
        return f"Error: {str(e)}", None

def run_script(script_name):
    """Run a Python script and display its output."""
    try:
        result = subprocess.run(["python3", script_name], text=True)
        if result.returncode != 0:
            print(Fore.RED + f"Error running {script_name}: {result.stderr.strip()}{Style.RESET_ALL}")
        else:
            print(Fore.GREEN + f"{script_name} executed successfully.{Style.RESET_ALL}")
            input(Fore.WHITE + "\n[0] Return to Main Menu" + Style.RESET_ALL)  # Wait for user input to return
    except Exception as e:
        print(Fore.RED + f"Error running {script_name}: {str(e)}{Style.RESET_ALL}")

def check_dependencies():
    print(Fore.WHITE + "Checking dependencies..." + Style.RESET_ALL)
    dependencies = ["python3", "adb", "fastboot"]
    for dep in dependencies:
        if subprocess.call(["which", dep], stdout=subprocess.PIPE, stderr=subprocess.PIPE) != 0:
            print(Fore.RED + f"{dep} is not installed. Please install it before running the tool.{Style.RESET_ALL}")
            exit(1)  # Exit if dependencies are not satisfied
    print(Fore.GREEN + "All dependencies are satisfied." + Style.RESET_ALL)

def main():
    check_dependencies()  # Automatically check dependencies at the start
    display_logo()
    
    while True:
        device_status, connection_type = get_device_status()
        print(Fore.WHITE + f"\nDevice Status:\n{device_status}{Style.RESET_ALL}")
        
        if connection_type == "fastboot":
            print(Fore.WHITE + "\nFastboot Menu:" + Style.RESET_ALL)
            print("[1] Exit Fastboot Mode")
            print("[2] Reboot to Recovery")
            print("[3] Flash ROM or Recovery")
            print()
            print("To exit, disconnect the device and enter (*) or force exit by (CTRL+C)")
            print()
        
            choice = input("Select an option: ")

            if choice == '1':
                run_script('exit_fastboot_mode.py')
            elif choice == '2':
                run_script('reboot_to_recovery.py')
            elif choice == '3':
                print(Fore.YELLOW + "Flash feature is coming soon..." + Style.RESET_ALL)
            elif choice == '*':
                print("Exiting...")
                break
            else:
                print(Fore.RED + "Invalid option. Please try again." + Style.RESET_ALL)

        elif connection_type == "adb":
            while True:
                print(Fore.WHITE + "\nADB Menu:" + Style.RESET_ALL)
                print("[1] Device Info")
                print("[2] Force Shutdown")
                print("[3] Restart Device")
                print("[4] Go to Fastboot")
                print("[5] Go to Bootloader")
                print("[6] Go to Recovery")
                print("[7] Flash Stock ROM")
                print("[8] Flash Custom Recovery")
                print()
                print("To exit, disconncet the device and enter (*) or force exit by (CTRL+C)")
                print()
                choice = input("Select an option: ")

                if choice == '1':
                    run_script('device_info.py')
                elif choice == '2':
                    run_script('force_shutdown.py')
                elif choice == '3':
                    run_script('restart_phone.py')
                elif choice == '4':
                    run_script('reboot_to_fastboot.py')
                elif choice == '5':
                    run_script('reboot_to_bootloader.py')
                elif choice == '6':
                    run_script('reboot_to_recovery.py')
                elif choice == '7':
                    print(Fore.YELLOW + "Sorry, this feature is under maintenance." + Style.RESET_ALL)
                elif choice == '8':
                    print(Fore.YELLOW + "Sorry, this feature is under maintenance." + Style.RESET_ALL)
                elif choice == '*':
                    print("Exiting...")
                    break
                else:
                    print(Fore.RED + "Invalid option. Please try again." + Style.RESET_ALL)

        else:
            print(Fore.RED + "No device connected. Please connect a device via ADB or Fastboot." + Style.RESET_ALL)
            print()
            print("To exit, disconncet the device and enter (*) or force exit by (CTRL+C)")
            print()
            choice = input("Select an option: ")
            if choice == '*':
                print("Exiting...")
                break
       
if __name__ == "__main__":
    main()

