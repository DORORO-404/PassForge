# ========= PassForge - Advanced Password Generator =========

# === Import Modules ===
import string
import random
from datetime import datetime
from colorama import Fore, Style, init
import pyfiglet
import sys

# === Initialize Colorama ===
init(autoreset=True)

# === Program Info ===
VERSION = "1.4"

# === Color Shortcuts ===
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

# === Display ASCII Banner ===
def display_banner():
    banner = pyfiglet.figlet_format("\nPassForge")
    print(f"{CYAN}{banner}{RESET}")
    print(f"""{CYAN}
╔═══════════════════════════════════════╗
║     {MAGENTA}PassForge - Password Generator{CYAN}    ║
║     {MAGENTA}Developer   : DORORO__404{CYAN}         ║
║     {MAGENTA}GitHub      : DORORO-404{CYAN}          ║
║     {MAGENTA}Version     : {VERSION}{CYAN}                 ║
╚═══════════════════════════════════════╝{RESET}
""")

# === Display Welcome Message ===
def display_welcome():
    print(f"{BLUE}[+] ===== {CYAN}Welcome to PassForge Password Generator{BLUE} ===== [+]{RESET}")

# === Safe Exit ===
def exit_passforge():
    print(f"\n{GREEN}Exiting PassForge... Thank you for using our tool!{RESET}")
    sys.exit()

# === Input Handler with Exit Options ===
def input_with_exit(prompt):
    try:
        user_input = input(prompt).strip()
        if user_input.lower() in ["exit", "quit", "q", "x", "close"]:
            exit_passforge()
        return user_input
    except KeyboardInterrupt:
        exit_passforge()

# === Prompt for Password Length ===
def get_password_length():
    while True:
        user_input = input_with_exit(f"{YELLOW}Enter the password length (minimum 8): {RESET}")
        try:
            length = int(user_input)
            if length < 8:
                print(f"{RED}Error: Password must be at least 8 characters.{RESET}")
            else:
                return length
        except ValueError:
            print(f"{RED}Invalid input. Please enter a valid number.{RESET}")

# === Prompt for Password Count ===
def get_password_count():
    while True:
        user_input = input_with_exit(f"{YELLOW}How many passwords to generate?: {RESET}")
        try:
            count = int(user_input)
            if count < 1:
                print(f"{RED}Error: Please enter a number greater than 0.{RESET}")
            else:
                return count
        except ValueError:
            print(f"{RED}Invalid input. Please enter a valid number.{RESET}")

# === Prompt for Password Mode ===
def choose_password_mode():
    print(f"\n{MAGENTA}[+] Available Password Modes:{RESET}")
    modes = [
        "[1] Numbers only", 
        "[2] Symbols only", 
        "[3] Mixed characters",
        "[4] Uppercase only",
        "[5] Lowercase only",
        "[6] Letters (uppercase + lowercase)"
    ]
    for mode in modes:
        print(f"{CYAN}{mode}{RESET}")

    while True:
        choice = input_with_exit(f"{YELLOW}Select a mode: {RESET}")
        options = {
            "1": "digits",
            "2": "symbols",
            "3": "mixed",
            "4": "uppercase",
            "5": "lowercase",
            "6": "letters"
        }
        if choice in options:
            return options[choice]
        else:
            print(f"{RED}Invalid selection. Please choose from 1 to 6.{RESET}")

# === Generate Password Based on Mode and Length ===
def generate_password(length, mode):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    if mode == "digits":
        chars = digits
    elif mode == "symbols":
        chars = symbols
    elif mode == "uppercase":
        chars = upper
    elif mode == "lowercase":
        chars = lower
    elif mode == "letters":
        chars = lower + upper
    elif mode == "mixed":
        mix = random.choices(lower, k=round(length * 0.2)) + \
              random.choices(upper, k=round(length * 0.2)) + \
              random.choices(digits, k=round(length * 0.1)) + \
              random.choices(symbols, k=round(length * 0.1))
        mix += random.choices(lower + upper + digits + symbols, k=length - len(mix))
        random.shuffle(mix)
        return ''.join(mix)
    else:
        raise ValueError("Unsupported password mode.")
    
    return ''.join(random.choices(chars, k=length))

# === Save Passwords to File ===
def save_passwords_to_file(passwords):
    filename = input_with_exit(f"{YELLOW}Enter a name for the file: {RESET}")
    with open(f"{filename}.txt", "w") as file:
        file.write(f"# Passwords generated on {datetime.now()}\n\n")
        for pw in passwords:
            file.write(pw + "\n")
    print(f"{GREEN}[✔] Passwords saved to {RESET}{MAGENTA}{filename}.txt{RESET}")

# === Generate and Display Passwords ===
def generate_and_display_passwords():
    length = get_password_length()
    count = get_password_count()
    mode = choose_password_mode()

    print(f"\n{MAGENTA}[+] Generating {count} passwords | Length: {length} | Mode: {mode.upper()}{RESET}")
    passwords = [generate_password(length, mode) for _ in range(count)]

    print(f"{GREEN}[✔] Passwords Generated Successfully:{RESET}\n")
    for idx, pw in enumerate(passwords, 1):
        print(f"{WHITE}{idx}. {pw}{RESET}")
    
    return passwords

# === Ask What to Do Next ===
def choose_next_action(passwords):
    print(f"\n{MAGENTA}[+] What would you like to do next?{RESET}")
    print(f"{CYAN}[1] Save the passwords to a file{RESET}")
    print(f"{CYAN}[2] Generate more passwords{RESET}")
    print(f"{CYAN}[3] Exit PassForge{RESET}")

    while True:
        choice = input_with_exit(f"{YELLOW}Select an option: {RESET}")
        if choice == "1":
            save_passwords_to_file(passwords)
            continue
        elif choice == "2":
            print(f"{GREEN}[✔] Generating more passwords...{RESET}\n")
            display_welcome()
            passwords = generate_and_display_passwords()
            continue

        elif choice == "3":
            exit_passforge()
        else:
            print(f"{RED}Invalid selection. Please choose 1, 2, or 3.{RESET}")

# === Show Version Info ===
def show_version():
    if "--version" in sys.argv:
        print(f"{CYAN}[•] PassForge Version: {VERSION}{RESET}")
        sys.exit()

# === Main Function ===
def main():
    show_version()
    display_banner()
    display_welcome()

    while True:
        passwords = generate_and_display_passwords()
        choose_next_action(passwords)

# === Entry Point ===
if __name__ == "__main__":
    main()
