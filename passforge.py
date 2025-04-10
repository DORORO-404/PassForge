# ===== PassForge: Advanced Password Generator =====

import string
import random
from datetime import datetime
import pyfiglet

# ANSI Escape Codes for color formatting
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
MAGENTA = "\033[1;35m"
RESET = "\033[0m"

# Show fancy banner using pyfiglet
def print_banner():
    ascii_banner = pyfiglet.figlet_format("PassForge")
    print(f"{MAGENTA}{ascii_banner}{RESET}")
    box = f"""{CYAN}
  ╔═══════════════════════════════════════╗
  ║     {MAGENTA}PassForge - Password Generator{CYAN}    ║
  ║     {MAGENTA}Developed by: DORORO{CYAN}              ║
  ║     {MAGENTA}Github: DORORO-404{CYAN}                ║
  ║     {MAGENTA}Version: 1.0{CYAN}                      ║
  ╚═══════════════════════════════════════╝{RESET}
    """
    print(box)

# Display welcome message
def print_title():
    print(f"{RED}[+] ====== {BLUE}Welcome to PassForge{RED} ====== [+]{RESET}")

# Get password length
def length_password():
    while True:
        user_input = input(f"{YELLOW}How many characters should the password have?: {RESET}")
        if user_input.lower() == "exit":
            print(f"{GREEN}Exiting PassForge...{RESET}")
            exit()
        try:
            length = int(user_input)
            if length < 8:
                print(f"{RED}❌ Password must be at least 8 characters long.{RESET}")
            else:
                return length
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a valid number.{RESET}")

# Get number of passwords to generate
def count_password():
    while True:
        user_input = input(f"{YELLOW}How many passwords would you like to generate?: {RESET}")
        if user_input.lower() == "exit":
            print(f"{GREEN}Exiting PassForge...{RESET}")
            exit()
        try:
            count = int(user_input)
            if count < 1:
                print(f"{RED}❌ Please enter a number greater than 0.{RESET}")
            else:
                return count
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a valid number.{RESET}")

# Generate password
def generate_password(length):
    password = []

    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digits = list(string.digits)
    symbols = list(string.punctuation)

    random.shuffle(lower)
    random.shuffle(upper)
    random.shuffle(digits)
    random.shuffle(symbols)

    num_lower = num_upper = round(length * 0.2)
    num_digits = num_symbols = round(length * 0.1)

    password += lower[:num_lower]
    password += upper[:num_upper]
    password += digits[:num_digits]
    password += symbols[:num_symbols]

    remaining = length - len(password)
    all_chars = lower + upper + digits + symbols
    password += [random.choice(all_chars) for _ in range(remaining)]

    return ''.join(random.sample(password, len(password)))

# Ask for file name
def get_file_name():
    while True:
        file_name = input(f"{YELLOW}Enter the file name to save passwords: {RESET}")
        if file_name.lower() == "exit":
            print(f"{GREEN}Exiting PassForge...{RESET}")
            exit()
        if file_name:
            return file_name
        else:
            print(f"{RED}❌ Invalid input. Please enter a valid file name.{RESET}")

# Save to file
def save_passwords(passwords):
    while True:
        save = input(f"\n{YELLOW}Do you want to save passwords in a file? [Y/n]: {RESET}").strip().lower()
        if save == "exit":
            print(f"{GREEN}Exiting PassForge...{RESET}")
            exit()
        if save in ["y", ""]:
            file_name = get_file_name()
            with open(f"{file_name}.txt", "w") as file:
                file.write(f"# Passwords generated on {datetime.now()}\n\n")
                for pw in passwords:
                    file.write(f"{pw}\n")
            print(f"{GREEN}✅ Passwords saved to '{file_name}.txt'{RESET}")
            break
        elif save == "n":
            break
        else:
            print(f"{RED}❌ Invalid input. Please enter 'y' for yes or 'n' for no.{RESET}")

# Ask to generate more
def generate_more_passwords():
    while True:
        repeat = input(f"{YELLOW}Generate more passwords? [Y/n]: {RESET}").strip().lower()
        if repeat == "exit":
            print(f"{GREEN}Exiting PassForge...{RESET}")
            exit()
        if repeat in ["y", ""]:
            break
        elif repeat == "n":
            print(f"{GREEN}Thank you for using PassForge. Goodbye!{RESET}")
            exit()
        else:
            print(f"{RED}❌ Invalid input. Please enter 'y' or 'n'.{RESET}")

# Main function
def main():
    print_banner()
    print_title()

    while True:
        length = length_password()
        count = count_password()

        passwords = [generate_password(length) for _ in range(count)]

        print(f"\n{BLUE}Generated Passwords:{RESET}")
        for idx, pw in enumerate(passwords, 1):
            print(f"{GREEN}{idx}. {pw}{RESET}")
        
        save_passwords(passwords)
        generate_more_passwords()

if __name__ == "__main__":
    main()
