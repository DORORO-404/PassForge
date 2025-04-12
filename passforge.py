# ===== PassForge: Advanced Password Generator =====

import string
import random
from datetime import datetime
import pyfiglet
import argparse
import os

# Program version
VERSION = "1.2"

# ANSI color codes (compatible with Kali Linux terminals)
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# Display the ASCII art banner using pyfiglet
def print_banner():
    ascii_banner = pyfiglet.figlet_format("  PassForge")
    print(f"{CYAN}{ascii_banner}{RESET}")
    box = f"""{BLUE}
  ╔═══════════════════════════════════════╗
  ║     PassForge - Password Generator    ║
  ║     Developed by: DORORO__404         ║
  ║     GitHub: DORORO-404                ║
  ║     Version: {VERSION}                      ║
  ╚═══════════════════════════════════════╝{RESET}
    """
    print(box)

# clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Print a welcome message
def print_title():
    print(f"\n\n{WHITE}[+] ===== {CYAN}Welcome to PassForge{WHITE} ===== [+]{RESET}")

# Ask user for desired password length
def length_password():
    while True:
        user_input = input(f"{YELLOW}Enter the password length: {RESET}")
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
            print(f"{RED}❌ Invalid input. Please enter a number.{RESET}")

# Ask user how many passwords to generate
def count_password():
    while True:
        user_input = input(f"{YELLOW}How many passwords do you want to generate?: {RESET}")
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

# Ask user which mode of characters to use
def mode_password():
    while True:
        options = [
            "[1] Numbers only", 
            "[4] Upper Letters",
            "[2] Symbols only", 
            "[5] Lower Letters",
            "[3] Mixed characters",
            "[6] Mixed Letters"
        ]

        print(f"\n")
        print(f"{CYAN}{options[0]:<25}{options[1]}{RESET}")
        print(f"{CYAN}{options[2]:<25}{options[3]}{RESET}")
        print(f"{CYAN}{options[4]:<25}{options[5]}{RESET}")

        choice = input(f"{YELLOW}Choice > {RESET}").strip().lower()
        if choice == "exit":
            print(f"{GREEN}Exiting PassForge...{RESET}")
            exit()
        try:
            choice = int(choice)
            if choice == 1:
                return "digits"
            elif choice == 2:
                return "symbols"
            elif choice == 3:
                return "mixed"
            elif choice == 4:
                return "upper letters"
            elif choice == 5:
                return "lower letters"
            elif choice == 6:
                return "mixed letters"
            else:
                print(f"{RED}❌ Invalid choice. Please select a number between 1 and 4.{RESET}")
        except ValueError:
            print(f"{RED}❌ Please enter a valid number (1-4).{RESET}")

# Generate a password based on the selected mode
def generate_password(length, mode):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digits = list(string.digits)
    symbols = list(string.punctuation)

    if mode == "digits":
        characters = digits
    elif mode == "symbols":
        characters = symbols
    elif mode == "mixed letters":
        characters = lower + upper
    elif mode == "upper letters":
        characters = upper
    elif mode == "lower letters":
        characters = lower
    elif mode == "mixed":
        num_lower = num_upper = round(length * 0.2)
        num_digits = num_symbols = round(length * 0.1)

        password = []
        password += random.sample(lower, min(num_lower, len(lower)))
        password += random.sample(upper, min(num_upper, len(upper)))
        password += random.sample(digits, min(num_digits, len(digits)))
        password += random.sample(symbols, min(num_symbols, len(symbols)))

        remaining = length - len(password)
        all_chars = lower + upper + digits + symbols
        password += [random.choice(all_chars) for _ in range(remaining)]

        return ''.join(random.sample(password, len(password)))
    else:
        raise ValueError("Invalid mode! Choose from: 'digits', 'symbols', 'letters', or 'mixed'.")

    return ''.join(random.choices(characters, k=length))

# Ask user for the file name to save the passwords
def get_file_name():
    while True:
        file_name = input(f"{YELLOW}Enter a file name to save the passwords: {RESET}")
        if file_name.lower() == "exit":
            print(f"{GREEN}Exiting PassForge...{RESET}")
            exit()
        if file_name:
            return file_name
        else:
            print(f"{RED}❌ File name cannot be empty.{RESET}")

# Save generated passwords to a text file
def save_passwords(passwords):
    while True:
        save = input(f"\n{YELLOW}Do you want to save the passwords to a file? [Y/n]: {RESET}").strip().lower()
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
            print(f"{RED}❌ Please enter 'y' for yes or 'n' for no.{RESET}")

# Ask the user whether to generate more passwords
def generate_more_passwords():
    while True:
        repeat = input(f"{YELLOW}Do you want to generate more passwords? [Y/n]: {RESET}").strip().lower()
        if repeat == "exit":
            print(f"{GREEN}Exiting PassForge...{RESET}")
            exit()
        if repeat in ["y", ""]:
            clear_screen()
            break
        elif repeat == "n":
            print(f"{GREEN}Thank you for using PassForge. Goodbye!{RESET}")
            exit()
        else:
            print(f"{RED}❌ Please enter 'y' or 'n'.{RESET}")

# Main function to run the generator
def main():
    clear_screen()
    print_banner()
    print_title()

    while True:
        length = length_password()
        count = count_password()
        mode = mode_password()

        passwords = [generate_password(length, mode) for _ in range(count)]

        print(f"\n{RED}Generated Passwords:{RESET}")
        for idx, pw in enumerate(passwords, 1):
            print(f"{GREEN}{idx}. {pw}{RESET}")

        save_passwords(passwords)
        generate_more_passwords()
        print_banner()
        print_title()

# Entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PassForge - Advanced Password Generator")
    parser.add_argument("--version", action="store_true", help="Show version and exit")
    args = parser.parse_args()

    if args.version:
        print(f"{CYAN}PassForge Version: {VERSION}{RESET}")
        exit()

    main()
