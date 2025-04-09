# ===== PassForge: Advanced Password Generator =====

# Import required modules
import string
import random
from datetime import datetime

# ANSI Escape Codes for color formatting
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

# Function to display the program title
def print_title():
    print(f"{RED}[+] ====== {BLUE}Welcome to PassForge{RED} ====== [+]{RESET}")

# Banner for PassForge
def show_banner():
    banner = f"""
┌──────────────────────────────────────────────────────────────┐
│   PassForge {YELLOW}v1.0{RESET} - Password Generator                        │
│   Developed by: {GREEN}dororo__404{RESET}                                  │
│   System: {BLUE}Kali Linux Ready 🐍{RESET}                                │
│   GitHub: {CYAN}https://github.com/DORORO-404{RESET}                      │
└──────────────────────────────────────────────────────────────┘
{YELLOW}🔐 Type 'exit' anytime to quit the program.{RESET}
"""
    print(banner)

# Ask for password length
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

# Ask how many passwords to generate
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

# Generate a single password
def generate_password(length):
    password = []

    lower_chars = list(string.ascii_lowercase)
    upper_chars = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    random.shuffle(lower_chars)
    random.shuffle(upper_chars)
    random.shuffle(digits)
    random.shuffle(punctuation)

    num_lower = num_upper = round(length * 0.2)
    num_digits = num_punct = round(length * 0.1)

    password += lower_chars[:num_lower]
    password += upper_chars[:num_upper]
    password += digits[:num_digits]
    password += punctuation[:num_punct]

    remaining = length - len(password)
    all_chars = lower_chars + upper_chars + digits + punctuation
    password += [random.choice(all_chars) for _ in range(remaining)]

    return ''.join(random.sample(password, len(password)))

# Get file name from user
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

# Save passwords to file
def save_passwords(passwords):
    while True:
        save = input(f"\n{YELLOW}Do you want to save passwords in a file? [Y/n]: {RESET}").strip().lower()
        if save == "exit":
            print(f"{GREEN}Exiting PassForge...{RESET}")
            exit()
        if save == "y" or save == "":
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

# Ask if the user wants to generate more passwords
def generate_more_passwords():
    while True:
        repeat = input(f"{YELLOW}Generate more passwords? [Y/n]: {RESET}").strip().lower()
        if repeat == "exit":
            print(f"{GREEN}Exiting PassForge...{RESET}")
            exit()
        if repeat == "y" or repeat == "":
            break
        elif repeat == "n":
            print(f"{GREEN}Thank you for using PassForge. Goodbye!{RESET}")
            exit()
        else:
            print(f"{RED}❌ Invalid input. Please enter 'y' for yes or 'n' for no.{RESET}")

# Main function to drive the program
def main():
    show_banner()
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

# Run if executed directly
if __name__ == "__main__":
    main()
