# ========= PassForge - Advanced Password Generator =========

# === Safe Import Modules ===
try:
    import os
    import sys
    import string
    import random
    import getpass
    from datetime import datetime
    import pyfiglet
    from colorama import Fore, Style, init
except ImportError as e:
    missing = str(e).split("'")[1]
    print(f"\n[!] Missing module: '{missing}'")
    print("[-] Please install all dependencies before running this script.")
    print("[*] Required: pyfiglet, colorama")
    print("[+] You can install them using:")
    print("[i] pip install pyfiglet colorama\n")
    sys.exit(1)

# === Initialize Colorama ===
init(autoreset=True, strip=False, convert=True)

# === Version Info ===
VERSION = "1.5"

# === Color Shortcuts ===
RED, GREEN, YELLOW = Fore.RED, Fore.GREEN, Fore.YELLOW
BLUE, MAGENTA, CYAN = Fore.BLUE, Fore.MAGENTA, Fore.CYAN
WHITE, RESET = Fore.WHITE, Style.RESET_ALL

# === Display ASCII Banner ===
def display_banner():
    print(f"{MAGENTA}{pyfiglet.figlet_format('PassForge')}{RESET}")
    print(f"""{CYAN}
╔════════════════════════════════════════════╗
║   {MAGENTA}PassForge - Advanced Password Generator{CYAN}  ║
║   {MAGENTA}By: DORORO__404   |  Version: v{VERSION}  {CYAN}     ║
╚════════════════════════════════════════════╝{RESET}
""")

# === Show Welcome Message and Usage Instructions ===
def display_welcome():
    print(f"\n{MAGENTA}[+] {GREEN}Welcome to {MAGENTA}PassForge{GREEN} — Create. Secure. Generate.{RESET}")
    print(f"{YELLOW}[i] {CYAN}Advanced password generator for strong and secure credentials.{RESET}")
    print(f"{YELLOW}[i] {CYAN}Let's forge a password that's hard to crack!{RESET}")
    print(f"{YELLOW}[i] Type '{CYAN}exit{YELLOW}', '{CYAN}quit{YELLOW}', '{CYAN}close{YELLOW}', or {CYAN}CTRL + C{YELLOW} to exit.{RESET}")
    print(f"{CYAN}{'-' * 75}{RESET}")

# === Graceful Exit Handler ===
def exit_passforge():
    print(f"\n{GREEN}[*] Exiting PassForge...{RESET}")
    print(f"{MAGENTA}[!] Thank you for trusting PassForge!{RESET}")
    print(f"{YELLOW}[i] Session ended successfully.\n{RESET}")
    sys.exit()

# === General Input Handler with Exit Support ===
def input_handler(message, is_password=False):
    try:
        while True:
            user_input = getpass.getpass(message).strip() if is_password else input(message).strip()
            if user_input.lower() in ["exit", "quit", "close"]:
                print(f"\n{YELLOW}[i] Exit command received.{RESET}")
                exit_passforge()
            elif not user_input:
                print(f"{RED}[!] Input cannot be empty. Please try again.{RESET}")
            else:
                return user_input
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}[i] Keyboard interrupt detected.{RESET}")
        exit_passforge()

# === Request Password Length from User ===
def get_password_length():
    while True:
        user_input = input_handler(f"\n{CYAN}[>] Enter desired password length (min 8): {RESET}")
        try:
            length = int(user_input)
            if length < 8:
                print(f"{RED}[!] Password length must be at least 8 characters.{RESET}")
            else:
                return length
        except ValueError:
            print(f"{RED}[!] Please enter a numeric value for the length.{RESET}")

# === Request Number of Passwords to Generate ===
def get_password_count():
    while True:
        user_input = input_handler(f"{CYAN}[>] How many passwords to generate?: {RESET}")
        try:
            count = int(user_input)
            if count < 1:
                print(f"{RED}[!] Please enter a number greater than 0.{RESET}")
            else:
                return count
        except ValueError:
            print(f"{RED}[!] Please enter a numeric value for the count.{RESET}")

# === Present Password Generation Modes ===
def choose_password_mode():
    print(f"\n{MAGENTA}[+] {GREEN}Available Password Modes:{RESET}")
    modes = {
        "1": "🔢 Numbers only",
        "2": "🔣 Symbols only",
        "3": "🧪 Mixed characters",
        "4": "🔠 Uppercase only",
        "5": "🔡 Lowercase only",
        "6": "🔤 Letters (uppercase + lowercase)"
    }

    options = {
        "1": "digits",
        "2": "symbols",
        "3": "mixed",
        "4": "uppercase",
        "5": "lowercase",
        "6": "letters"
    }

    for key, desc in modes.items():
        print(f"{GREEN}[{key}] {WHITE}{desc}{RESET}")

    while True:
        choice = input_handler(f"{CYAN}[>] Select a mode: {RESET}")
        if choice in options:
            return options[choice]
        print(f"{RED}[!] Invalid selection '{WHITE}{choice}{RED}'. Choose 1 to 6.{RESET}")

# === Generate a Password Based on Length and Mode ===
def generate_password(length, mode):
    lower, upper, digits, symbols = string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation

    if mode == "mixed":
        base = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(symbols)
        ]
        remaining = random.choices(lower + upper + digits + symbols, k=length - 4)
        all_chars = base + remaining
        random.shuffle(all_chars)
        return ''.join(all_chars)

    charset = {
        "digits": digits,
        "symbols": symbols,
        "uppercase": upper,
        "lowercase": lower,
        "letters": lower + upper
    }.get(mode)

    if not charset:
        raise ValueError("Unsupported password mode.")
    return ''.join(random.choices(charset, k=length))

# === Save Generated Passwords to a Text File ===
def save_passwords_to_file(passwords):
    filename = input_handler(f"\n{CYAN}[>] Enter a name for the file: {RESET}")
    if os.path.exists(f"{filename}.txt"):
        overwrite = input_handler(f"{RED}[!] File '{filename}.txt' already exists. Overwrite? (y/n): {RESET}")
        if overwrite.lower() != 'y':
            print(f"{YELLOW}[i] Operation cancelled. No file was saved.{RESET}")
            return
    with open(f"{filename}.txt", "w") as file:
        file.write(f"# Passwords generated on {datetime.now()}\n\n")
        file.writelines(pw + "\n" for pw in passwords)
    print(f"{GREEN}[✔] Passwords saved to {MAGENTA}{filename}.txt{RESET}")

# === Generate and Display Passwords to User ===
def generate_and_display_passwords():
    length = get_password_length()
    count = get_password_count()
    mode = choose_password_mode()

    print(f"\n{MAGENTA}[+] Generating {count} password(s) | Length: {length} | Mode: {mode.upper()}{RESET}")
    passwords = [generate_password(length, mode) for _ in range(count)]

    print(f"{GREEN}[✔] Passwords Generated Successfully:{RESET}\n")
    for idx, pw in enumerate(passwords, 1):
        print(f"{WHITE}{idx}. {pw}{RESET}")
    return passwords

# === Present Options After Password Generation ===
def choose_next_action(passwords):
    while True:
        print(f"\n{MAGENTA}[+] {GREEN}What would you like to do next?{RESET}")
        print(f"{GREEN}[1] 💾 {WHITE}Save to file{RESET}")
        print(f"{GREEN}[2] 🔁 {WHITE}Generate more{RESET}")
        print(f"{GREEN}[3] 🚪 {WHITE}Exit PassForge{RESET}")

        choice = input_handler(f"{CYAN}[>] Select an option: {RESET}")

        if choice == "1":
            save_passwords_to_file(passwords)
        elif choice == "2":
            print(f"\n{GREEN}[✔] Generating more passwords...{RESET}")
            passwords = generate_and_display_passwords()
        elif choice == "3":
            print(f"\n{YELLOW}[i] Exit command received.{RESET}")
            exit_passforge()
        else:
            print(f"{RED}[!] Invalid selection '{WHITE}{choice}{RED}'. Choose 1, 2, or 3.{RESET}")

# === Menu options ===
def choose_option():
    while True:
        print(f"\n{MAGENTA}[+] {GREEN}What would you like to do?{RESET}")
        print(f"{GREEN}[1] 🧩 {WHITE}Generate Passwords{RESET}")
        print(f"{GREEN}[2] 🚪 {WHITE}Exit PassForge{RESET}")
        choice = input_handler(f"{CYAN}[>] Enter your choice: {RESET}")

        if choice == '1':
            passwords = generate_and_display_passwords()
            choose_next_action(passwords)
        elif choice == '2':
            print(f"\n{YELLOW}[i] Exit command received.{RESET}")
            exit_passforge()
        else:
            print(f"{RED}[!] Invalid option '{WHITE}{choice}{RED}'. Choose 1 or 2.{RESET}")

# === Handle Version Display if --version Flag is Used ===
def show_version():
    if "--version" in sys.argv:
        print(f"{CYAN}[•] PassForge Version: {VERSION}{RESET}")
        sys.exit()

# === Main function ===
def main():
    show_version()
    display_banner()
    display_welcome()

    try:
        while True:
            choose_option()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}[i] Keyboard interrupt detected.{RESET}")
        exit_passforge()
    except Exception as e:
        print(f"\n{RED}[!] Unexpected error: {WHITE}{e}{RESET}")
        exit_passforge()

# === Entry Point ===
if __name__ == "__main__":
    main()
