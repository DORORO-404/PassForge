# ========= PassForge - Password Generator =========

# === Import necessary modules ===
import string
import random
from datetime import datetime
import pyfiglet
import sys

# ===== Program Info =====
VERSION = "1.3"

# ===== ANSI Color Codes =====
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ===== Display the ASCII banner using pyfiglet =====
def print_banner():
    ascii_banner = pyfiglet.figlet_format("\n\n  PassForge")
    print(f"{MAGENTA}{ascii_banner}{RESET}")
    box = f"""{CYAN}
  ╔═══════════════════════════════════════╗
  ║     {MAGENTA}PassForge - Password Generator {CYAN}   ║
  ║     {MAGENTA}Developed by: DORORO__404{CYAN}         ║
  ║     {MAGENTA}GitHub: DORORO-404{CYAN}                ║
  ║     {MAGENTA}Version: {VERSION}{CYAN}                      ║
  ╚═══════════════════════════════════════╝{RESET}
    """
    print(box)

# ===== Display welcome title =====
def print_title():
    print(f"\n{RED}[+] ===== {CYAN}Welcome to PassForge Password Generator{RED} ===== [+]{RESET}")

# === Exit safely with a message ===
def exit_program():
    print(f"{GREEN}Exiting PassForge...{RESET}")
    sys.exit()

# === Handle input and check for exit keywords ===
def safe_input(prompt):
    try:
        user_input = input(prompt).strip()
        if user_input.lower() in ["exit", "quit", "q", "x", "close"]:
            exit_program()
        return user_input
    except KeyboardInterrupt:
        print(f"\n{GREEN}Exiting PassForge...{RESET}")
        sys.exit()

# ===== Ask user for password length =====
def length_password():
    while True:
        user_input = safe_input(f"{YELLOW}Enter the desired password length: {RESET}")
        try:
            length = int(user_input)
            if length < 8:
                print(f"{RED}Password must be at least 8 characters long.{RESET}")
            else:
                return length
        except ValueError:
            print(f"{RED}Invalid input. Please enter a valid number.{RESET}")

# ===== Ask user how many passwords to generate =====
def count_password():
    while True:
        user_input = safe_input(f"{YELLOW}How many passwords would you like to generate?: {RESET}")
        try:
            count = int(user_input)
            if count < 1:
                print(f"{RED}Please enter a number greater than 0.{RESET}")
            else:
                return count
        except ValueError:
            print(f"{RED}Invalid input. Please enter a valid number.{RESET}")

# ===== Ask user to choose password mode =====
def mode_password():
    while True:
        options = [
            "[1] Numbers only", 
            "[4] Uppercase letters",
            "[2] Symbols only", 
            "[5] Lowercase letters",
            "[3] Mixed characters",
            "[6] Mixed letters"
        ]

        print(f"\n")
        print(f"{CYAN}{options[0]:<25}{options[1]}{RESET}")
        print(f"{CYAN}{options[2]:<25}{options[3]}{RESET}")
        print(f"{CYAN}{options[4]:<25}{options[5]}{RESET}")

        choice = safe_input(f"{YELLOW}Select an option: {RESET}")
        try:
            choice = int(choice)
            if choice == 1:
                return "digits"
            elif choice == 2:
                return "symbols"
            elif choice == 3:
                return "mixed"
            elif choice == 4:
                return "uppercase"
            elif choice == 5:
                return "lowercase"
            elif choice == 6:
                return "letters"
            else:
                print(f"{RED}Invalid choice. Please select a number between 1 and 6.{RESET}")
        except ValueError:
            print(f"{RED}Please enter a valid number (1–6).{RESET}")

# ===== Generate a password based on mode and length =====
def generate_password(length, mode):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digits = list(string.digits)
    symbols = list(string.punctuation)

    if mode == "digits":
        characters = digits
    elif mode == "symbols":
        characters = symbols
    elif mode == "letters":
        characters = lower + upper
    elif mode == "uppercase":
        characters = upper
    elif mode == "lowercase":
        characters = lower
    elif mode == "mixed":
        num_lower = num_upper = round(length * 0.2)
        num_digits = num_symbols = round(length * 0.1)

        password = []
        password += random.choices(lower, k=num_lower)
        password += random.choices(upper, k=num_upper)
        password += random.choices(digits, k=num_digits)
        password += random.choices(symbols, k=num_symbols)

        remaining = length - len(password)
        all_chars = lower + upper + digits + symbols
        password += [random.choice(all_chars) for _ in range(remaining)]

        return ''.join(random.sample(password, len(password)))
    else:
        raise ValueError("Invalid mode selected.")

    return ''.join(random.choices(characters, k=length))

# ===== Ask user for file name to save passwords =====
def get_file_name():
    while True:
        file_name = safe_input(f"{YELLOW}Enter a name for the output file: {RESET}")
        if file_name.strip():
            return file_name.strip()
        else:
            print(f"{RED}File name cannot be empty.{RESET}")

# ===== Save generated passwords to a text file =====
def save_passwords(passwords):
    while True:
        save = safe_input(f"\n{YELLOW}Do you want to save the passwords to a file? [Y/n]: {RESET}").lower()
        if save in ["y", ""]:
            file_name = get_file_name()
            with open(f"{file_name}.txt", "w") as file:
                file.write(f"# Passwords generated on {datetime.now()}\n\n")
                for pw in passwords:
                    file.write(f"{pw}\n")
            print(f"{GREEN}Passwords saved to '{file_name}.txt'{RESET}")
            break
        elif save == "n":
            break
        else:
            print(f"{RED}Please enter 'y' for yes or 'n' for no.{RESET}")

# ===== Ask user if they want to generate more passwords =====
def generate_more_passwords():
    while True:
        repeat = safe_input(f"{YELLOW}Would you like to generate more passwords? [Y/n]: {RESET}").lower()
        if repeat in ["y", ""]:
            break
        elif repeat == "n":
            print(f"{GREEN}Thank you for using PassForge. Goodbye!{RESET}")
            exit()
        else:
            print(f"{RED}Please enter 'y' or 'n'.{RESET}")

# ===== Main function that runs the program =====
def main():
    if "--version" in sys.argv or "-v" in sys.argv:
        print(f"{CYAN}PassForge Version: {VERSION}{RESET}")
        sys.exit()

    print_banner()

    while True:
        print_title()

        length = length_password()
        count = count_password()
        mode = mode_password()

        print(f"\n{CYAN}[+] Generating {count} password(s) | Length: {length} | Mode: {mode.upper()}{RESET}")
        print(f"{RED}Generated Passwords:{RESET}")
        passwords = [generate_password(length, mode) for _ in range(count)]

        for idx, pw in enumerate(passwords, 1):
            print(f"{GREEN}{idx}. {pw}{RESET}")

        save_passwords(passwords)
        generate_more_passwords()

# ===== Entry Point =====
if __name__ == "__main__":
    main()
