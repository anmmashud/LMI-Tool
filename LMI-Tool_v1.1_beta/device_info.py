import subprocess
from colorama import Fore, Style

def get_property(prop):
    """Helper function to retrieve a system property from the device via ADB."""
    try:
        result = subprocess.run(["adb", "shell", f"getprop {prop}"], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error retrieving {prop}: {str(e)}"

def get_storage_info():
    """Retrieve the total, used, and available storage capacity in GB."""
    try:
        # Get storage information for the /data partition
        result = subprocess.run(["adb", "shell", "df", "/data"], capture_output=True, text=True)
        lines = result.stdout.strip().split("\n")
        if len(lines) > 1:
            storage_info = lines[1].split()
            total_storage = int(storage_info[1]) // (1024**2)  # Convert to GB
            used_storage = int(storage_info[2]) // (1024**2)   # Convert to GB
            available_storage = int(storage_info[3]) // (1024**2)  # Convert to GB
            return f"{total_storage} GB", f"{used_storage} GB", f"{available_storage} GB"
        return "Unknown", "Unknown", "Unknown"
    except Exception as e:
        return f"Error retrieving storage info: {str(e)}", "Unknown", "Unknown"

def get_memory_info():
    """Retrieve the total and used RAM capacity."""
    try:
        result = subprocess.run(["adb", "shell", "cat /proc/meminfo"], capture_output=True, text=True)
        lines = result.stdout.strip().split("\n")
        total_mem = None
        free_mem = None
        for line in lines:
            if "MemTotal" in line:
                total_mem = line.split()[1]
            elif "MemAvailable" in line:
                free_mem = line.split()[1]
        if total_mem and free_mem:
            used_mem = int(total_mem) - int(free_mem)
            return f"{int(total_mem) // 1024} MB", f"{used_mem // 1024} MB"
        return "Unknown", "Unknown"
    except Exception as e:
        return f"Error retrieving memory info: {str(e)}", "Unknown"

def is_rooted():
    """Check if the device is rooted."""
    try:
        result = subprocess.run(["adb", "shell", "su -c 'id'"], capture_output=True, text=True)
        return "Rooted" if "uid=0" in result.stdout else "Not Rooted"
    except Exception as e:
        return f"Error checking root status: {str(e)}"

def get_bootloader_status():
    """Check if the bootloader is unlocked or locked."""
    try:
        result = subprocess.run(["adb", "shell", "getprop ro.boot.flash.locked"], capture_output=True, text=True)
        return "Unlocked" if result.stdout.strip() == "0" else "Locked"
    except Exception as e:
        return f"Error retrieving bootloader status: {str(e)}"

def get_recovery_type():
    """Check if the recovery is stock, TWRP, or other."""
    try:
        result = subprocess.run(["adb", "shell", "getprop ro.boot.recovery"], capture_output=True, text=True)
        recovery_name = result.stdout.strip().lower()
        if "twrp" in recovery_name:
            return "TWRP"
        elif "orangefox" in recovery_name:
            return "OrangeFox"
        else:
            return "Stock" if not recovery_name else "Other"
    except Exception as e:
        return f"Error retrieving recovery type: {str(e)}"

def get_rom_info():
    """Check if the ROM is stock or custom."""
    try:
        build_fingerprint = get_property("ro.build.fingerprint")
        if "xiaomi" in build_fingerprint.lower():
            return "Stock ROM"
        else:
            return "Custom ROM"
    except Exception as e:
        return f"Error retrieving ROM info: {str(e)}"

def display_device_info():
    print(Fore.CYAN + "Gathering device information..." + Style.RESET_ALL)

    # Get the device info using adb shell getprop
    model_name = get_property("ro.product.device") + " (" + get_property("ro.product.model") + ")"
    cpu_model = get_property("ro.product.board") + " (" + get_property("ro.board.platform") + ")"
    android_version = get_property("ro.build.version.release")
    miui_version = get_property("ro.miui.ui.version.name")
    
    total_ram, used_ram = get_memory_info()
    total_storage, used_storage, available_storage = get_storage_info()
    root_status = is_rooted()
    bootloader_status = get_bootloader_status()
    recovery_type = get_recovery_type()
    rom_info = get_rom_info()

    # Display the gathered information
    print(Fore.WHITE + "\nDevice Information:" + Style.RESET_ALL)
    print(f"{Fore.GREEN}Model Name: {model_name}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}CPU Model: {cpu_model}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}RAM: {used_ram} used / {total_ram} total{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Storage: {used_storage} used / {total_storage} total / {available_storage} available{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Android Version: {android_version}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}MIUI Version: {miui_version}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Bootloader: {bootloader_status}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Root Status: {root_status}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Recovery: {recovery_type}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Installed ROM: {rom_info}{Style.RESET_ALL}")

if __name__ == "__main__":
    display_device_info()
