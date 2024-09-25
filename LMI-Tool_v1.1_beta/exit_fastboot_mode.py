import subprocess

def exit_fastboot_mode():
    try:
        subprocess.run(["fastboot", "reboot"], check=True)
        print("Exiting fastboot mode.")
    except subprocess.CalledProcessError:
        print("Error: Unable to exit fastboot mode.")

if __name__ == "__main__":
    exit_fastboot_mode()

