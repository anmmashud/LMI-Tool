#!/usr/bin/env python3
import subprocess

def force_shutdown():
    print("Forcing shutdown...")
    subprocess.run(["adb", "shell", "reboot", "-p"])

def main():
    force_shutdown()
    print("Force shutdown command executed.")

if __name__ == "__main__":
    main()
