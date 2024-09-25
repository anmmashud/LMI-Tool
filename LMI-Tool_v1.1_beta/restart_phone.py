import subprocess

def restart_phone():
    try:
        subprocess.run(["adb", "reboot"], check=True)
        print("Device is restarting.")
    except subprocess.CalledProcessError:
        print("Error: Unable to restart device.")

if __name__ == "__main__":
    restart_phone()
