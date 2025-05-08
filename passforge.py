# ========= PassForge - Advanced Password Generator =========
# Developed by dororo__404 | Version: 1.5.1

# === [IMPORT] Required Modules ===
try:
    import os
    import sys
    import string
    import random
    import getpass
    import pyfiglet
    from datetime import datetime
except ImportError as e:
    missing = str(e).split("'")[1]
    print(f"\n\033[91m[ERROR] Missing module: '{missing}'\033[0m")
    print("\033[93m[WARNING] Please install all required dependencies before running this script.\033[0m")
    print("\033[94m[INFO] Required module: pyfiglet\033[0m")
    print("\033[92m[SUGGESTION] You can install it directly using:\033[0m")
    print("\033[96m  → pip install pyfiglet\033[0m\n")

    print("\033[95m[RECOMMENDED] Set up a virtual environment:\033[0m")
    print("\033[97m  # For Linux / macOS:\033[0m")
    print("\033[96m    python3 -m venv venv && source venv/bin/activate\033[0m")
    print("\033[97m  # For Windows:\033[0m")
    print("\033[96m    python -m venv venv && venv\\Scripts\\activate\033[0m\n")

    print("\033[92m[THEN] Install all requirements from file (if available):\033[0m")
    print("\033[96m  → pip install -r requirements.txt\033[0m\n")

    sys.exit(1)

# === [CONFIG] ANSI Colors for Output ===
RESET   = "\033[0m"
BOLD    = "\033[1m"
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"

# === [INFO] Version Number ===
VERSION = "1.5.1"

# === [UI] Display ASCII Banner ===
def display_banner():
    print(f"{MAGENTA}{pyfiglet.figlet_format('PassForge')}{RESET}")
    print(f"""{CYAN}
╔════════════════════════════════════════════╗
║   {MAGENTA}PassForge - Advanced Password Generator{CYAN}  ║
║   {MAGENTA}By: DORORO__404   |  Version: v{VERSION}  {CYAN}     ║
╚════════════════════════════════════════════╝{RESET}
""")

# === [UI] Welcome Message ===
def display_welcome():
    print(f"\n{MAGENTA}[+] Welcome to {GREEN}PassForge{MAGENTA} — Create. Secure. Generate.{RESET}")
    print(f"{YELLOW}[INFO] An advanced password generator for strong and secure credentials.{RESET}")
    print(f"{YELLOW}[INFO] Type '{CYAN}exit{YELLOW}', '{CYAN}quit{YELLOW}', '{CYAN}close{YELLOW}', or press {CYAN}CTRL + C{YELLOW} to exit.{RESET}")
    print(f"{CYAN}{'-' * 75}{RESET}")

# === [EXIT] Graceful Exit Handler ===
def exit_passforge():
    print(f"\n{GREEN}[INFO] Exiting PassForge...{RESET}")
    print(f"{MAGENTA}[THANK YOU] Thank you for using PassForge!{RESET}")
    print(f"{YELLOW}[INFO] Session ended successfully.{RESET}\n")
    sys.exit()

# === [INPUT] Unified Input with Exit Support ===
def input_handler(message, is_password=False):
    try:
        while True:
            user_input = getpass.getpass(message).strip() if is_password else input(message).strip()
            if user_input.lower() in ["exit", "quit", "close"]:
                print(f"{YELLOW}[INFO] Exit command received.{RESET}")
                exit_passforge()
            elif not user_input:
                print(f"{RED}[ERROR] Input cannot be empty. Please try again.{RESET}")
            else:
                return user_input
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[INFO] Keyboard interrupt detected.{RESET}")
        exit_passforge()

# === [LOGIC] Get Password Length ===
def get_password_length():
    while True:
        user_input = input_handler(f"\n{CYAN}[INPUT] Enter desired password length: {RESET}")
        try:
            length = int(user_input)
            if length < 8:
                print(f"{RED}[ERROR] Password length must be at least 8 characters.{RESET}")
            else:
                return length
        except ValueError:
            print(f"{RED}[ERROR] Please enter a numeric value for the length.{RESET}")

# === [LOGIC] Get Number of Passwords ===
def get_password_count():
    while True:
        user_input = input_handler(f"{CYAN}[INPUT] Enter number of passwords to generate: {RESET}")
        try:
            count = int(user_input)
            if count < 1:
                print(f"{RED}[ERROR] Please enter a number greater than 0.{RESET}")
            else:
                return count
        except ValueError:
            print(f"{RED}[ERROR] Please enter a numeric value for the count.{RESET}")

# === [LOGIC] Choose Generation Mode ===
def choose_password_mode():
    print(f"\n{MAGENTA}[+] Available Password Modes:{RESET}")
    modes = {
        "1": "Numbers only",
        "2": "Symbols only",
        "3": "Mixed characters",
        "4": "Uppercase letters only",
        "5": "Lowercase letters only",
        "6": "Letters (uppercase + lowercase)"
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
        choice = input_handler(f"{CYAN}[INPUT] Select a mode: {RESET}")
        if choice in options:
            return options[choice]
        print(f"{RED}[ERROR] Invalid selection '{WHITE}{choice}{RED}'. Choose 1 to 6.{RESET}")

# === [GENERATION] Generate Password Based on Mode ===
def generate_password(length, mode):
    lower, upper, digits, symbols = string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation
    if mode == "mixed":
        base = [random.choice(lower), random.choice(upper), random.choice(digits), random.choice(symbols)]
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

# === [STORAGE] Save Passwords to File ===
def save_passwords_to_file(passwords):
    filename = input_handler(f"\n{CYAN}[INPUT] Enter file name to save: {RESET}")
    path = f"{filename}.txt"
    if os.path.exists(path):
        overwrite = input_handler(f"{YELLOW}[WARNING] File '{path}' exists. Overwrite? [Y/n]: {RESET}")
        if overwrite.lower() != 'y':
            print(f"{YELLOW}[INFO] Operation cancelled. No file was saved.{RESET}")
            return
    with open(path, "w") as file:
        file.write(f"# Passwords generated on {datetime.now()}\n\n")
        file.writelines(pw + "\n" for pw in passwords)
    print(f"{GREEN}[SUCCESS] Passwords saved to {MAGENTA}{filename}.txt{RESET}")

# === [OUTPUT] Generate and Display Passwords ===
def generate_and_display_passwords():
    length = get_password_length()
    count = get_password_count()
    mode = choose_password_mode()

    if count > 1:
        print(f"\n{MAGENTA}[+] Generating {count} passwords | Length: {length} | Mode: {mode.upper()}{RESET}")
    else:
        print(f"\n{MAGENTA}[+] Generating {count} password | Length: {length} | Mode: {mode.upper()}{RESET}")

    passwords = [generate_password(length, mode) for _ in range(count)]
    print(f"{GREEN}[SUCCESS] Passwords generated successfully:{RESET}\n")
    for idx, pw in enumerate(passwords, 1):
        print(f"{WHITE}{idx}. {pw}{RESET}")
    return passwords

# === [UI] Post-generation Options Menu ===
def choose_next_action(passwords):
    while True:
        print(f"\n{MAGENTA}[+] What would you like to do next?{RESET}")
        print(f"{GREEN}[1] {WHITE}Save to file{RESET}")
        print(f"{GREEN}[2] {WHITE}Generate more passwords{RESET}")
        print(f"{GREEN}[3] {WHITE}Exit PassForge{RESET}")
        choice = input_handler(f"{CYAN}[INPUT] Select an option: {RESET}")
        if choice == "1":
            save_passwords_to_file(passwords)
        elif choice == "2":
            passwords = generate_and_display_passwords()
        elif choice == "3":
            exit_passforge()
        else:
            print(f"{RED}[ERROR] Invalid selection '{WHITE}{choice}{RED}'. Choose 1, 2, or 3.{RESET}")

# === [UI] Main Menu ===
def choose_option():
    while True:
        print(f"\n{MAGENTA}[+] What would you like to do?{RESET}")
        print(f"{GREEN}[1] {WHITE}Generate Passwords{RESET}")
        print(f"{GREEN}[2] {WHITE}Exit PassForge{RESET}")
        choice = input_handler(f"{CYAN}[INPUT] Enter your choice: {RESET}")
        if choice == '1':
            passwords = generate_and_display_passwords()
            choose_next_action(passwords)
        elif choice == '2':
            exit_passforge()
        else:
            print(f"{RED}[ERROR] Invalid option '{WHITE}{choice}{RED}'. Choose 1 or 2.{RESET}")

# === [FLAG] Handle --version argument ===
def show_version():
    if "--version" in sys.argv:
        print(f"{CYAN}[INFO] PassForge Version: {VERSION}{RESET}")
        sys.exit()

# === [MAIN] Entry Point ===
def main():
    show_version()
    display_banner()
    display_welcome()
    try:
        while True:
            choose_option()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[INFO] Keyboard interrupt detected.{RESET}")
        exit_passforge()
    except Exception as e:
        print(f"\n{RED}[ERROR] Unexpected error: {WHITE}{e}{RESET}")
        exit_passforge()

if __name__ == "__main__":
    main()
