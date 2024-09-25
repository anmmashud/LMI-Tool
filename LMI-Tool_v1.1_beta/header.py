
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def type_out(text, delay=0.05):
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

display_logo()


