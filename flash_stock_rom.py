import subprocess
import os
import sys

def flash_stock_rom():
    print("Rebooting into fastboot mode...")
    try:
        subprocess.run(["adb", "reboot", "bootloader"], check=True)
        print("Device entered fastboot mode successfully.")

        # Ask for the ROM file
        rom_file = input("Please enter the path to the ROM file (.tgz): ")
        
        # Extract the ROM file
        if not os.path.isfile(rom_file):
            print("Error: ROM file not found.")
            sys.exit(1)

        print("Extracting ROM file...")
        subprocess.run(["tar", "-xzf", rom_file], check=True)
        
        # Locate the flash_all.sh script
        flash_script = "flash_all.sh"
        if not os.path.isfile(flash_script):
            print("Error: flash_all.sh not found in the extracted files.")
            sys.exit(1)

        # Make the script executable
        subprocess.run(["chmod", "+x", flash_script], check=True)

        # Run the flash_all.sh script
        print("Flashing ROM...")
        subprocess.run(["./" + flash_script], check=True)
        print("Stock ROM flashing completed.")

    except subprocess.CalledProcessError:
        print("Error: An error occurred during flashing.")

if __name__ == "__main__":
    flash_stock_rom()

