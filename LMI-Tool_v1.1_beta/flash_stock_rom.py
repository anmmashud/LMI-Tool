import subprocess
import os
import sys
import time

def flash_stock_rom():
    print("Rebooting into fastboot mode...")
    try:
        subprocess.run(["adb", "reboot", "bootloader"], check=True)
        print("Device entered fastboot mode successfully.")
        time.sleep(5)  # Wait a few seconds to ensure device is in fastboot mode

        # Ask for the ROM file
        rom_file = input("Please enter the path to the ROM file (.tgz, .tar.gz, .zip): ")
        
        # Verify the ROM file exists
        if not os.path.isfile(rom_file):
            print("Error: ROM file not found.")
            sys.exit(1)

        # Extract the ROM file
        print("Extracting ROM file...")
        if rom_file.endswith('.tgz') or rom_file.endswith('.tar.gz'):
            subprocess.run(["tar", "-xzf", rom_file], check=True)
        elif rom_file.endswith('.zip'):
            subprocess.run(["unzip", rom_file], check=True)
        else:
            print("Error: Unsupported file type. Please provide a .tgz, .tar.gz, or .zip file.")
            sys.exit(1)
        
        # Locate the flash_all.sh script
        flash_script = "flash_all.sh"
        if not os.path.isfile(flash_script):
            print("Error: flash_all.sh not found in the extracted files.")
            sys.exit(1)

        # Make the script executable
        print("Making the flashing script executable...")
        subprocess.run(["chmod", "+x", flash_script], check=True)

        # Run the flash_all.sh script
        print("Flashing ROM...")
        subprocess.run(["./" + flash_script], check=True)
        print("Stock ROM flashing completed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error: An error occurred during flashing. {e}")
        sys.exit(1)

if __name__ == "__main__":
    flash_stock_rom()
