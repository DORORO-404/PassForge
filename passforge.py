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
RESET = "\033[0m"

# Function to display the program title
def print_title():
    """Display the welcome title."""
    print(f"{RED}[+] ====== {BLUE}Welcome to PassForge{RED} ====== [+]{RESET}")

# Function to ask for password length
def length_password():
    """Prompt user to enter the desired password length."""
    while True:
        try:
            length = int(input(f"{YELLOW}How many characters should the password have?: {RESET}"))
            if length < 8:
                print(f"{RED}❌ Password must be at least 8 characters long.{RESET}")
            else:
                return length
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a valid number.{RESET}")

# Function to ask how many passwords to generate
def count_password():
    """Prompt user to enter the number of passwords to generate."""
    while True:
        try:
            count = int(input(f"{YELLOW}How many passwords would you like to generate?: {RESET}"))
            if count < 1:
                print(f"{RED}❌ Please enter a number greater than 0.{RESET}")
            else:
                return count
        except ValueError:
            print(f"{RED}❌ Invalid input. Please enter a valid number.{RESET}")

# Function to generate a single password
def generate_password(length):
    """Generate a random password of the given length."""
    password = []

    # Define character sets
    lower_chars = list(string.ascii_lowercase)
    upper_chars = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    # Shuffle the character sets for randomness
    random.shuffle(lower_chars)
    random.shuffle(upper_chars)
    random.shuffle(digits)
    random.shuffle(punctuation)

    # Define how many characters to take from each set
    num_lower = num_upper = round(length * 0.2)  # 20% lower + 20% upper
    num_digits = num_punct = round(length * 0.1)  # 10% digits + 10% punctuation

    # Add characters from each set
    password += lower_chars[:num_lower]
    password += upper_chars[:num_upper]
    password += digits[:num_digits]
    password += punctuation[:num_punct]

    # Fill remaining characters randomly
    remaining = length - len(password)
    all_chars = lower_chars + upper_chars + digits + punctuation
    password += [random.choice(all_chars) for _ in range(remaining)]

    # Shuffle and return the final password
    return ''.join(random.sample(password, len(password)))

# Function to get the file name from the user
def get_file_name():
    """Prompt user for the file name to save passwords."""
    while True:
        file_name = input(f"{YELLOW}Enter the file name to save passwords: {RESET}")
        if file_name:
            return file_name
        else:
            print(f"{RED}❌ Invalid input. Please enter a valid file name.{RESET}")

# Function to save generated passwords to a file
def save_passwords(passwords):
    """Ask the user if they want to save the passwords to a file."""
    while True:
        save = input(f"\n{YELLOW}Do you want to save passwords in a file? [Y/n]: {RESET}").strip().lower()
        if save == "y" or save == "":  # User wants to save
            file_name = get_file_name()
            with open(f"{file_name}.txt", "w") as file:
                file.write(f"Passwords generated on {datetime.now()}\n\n")
                for pw in passwords:
                    file.write(f"{pw}\n")
            print(f"{GREEN}✅ Passwords saved to '{file_name}.txt'{RESET}")
            break
        elif save == "n":  # User does not want to save
            break
        else:  # Invalid input
            print(f"{RED}❌ Invalid input. Please enter 'y' for yes or 'n' for no.{RESET}")

# Function to ask if the user wants to generate more passwords
def generate_more_passwords():
    """Prompt user to generate more passwords or exit."""
    while True:
        repeat = input(f"{YELLOW}Generate more passwords? [Y/n]: {RESET}").strip().lower()
        if repeat == "y" or repeat == "":  # User wants to generate more passwords
            break
        elif repeat == "n":  # User does not want to generate more
            print(f"{GREEN}Thank you for using PassForge. Goodbye!{RESET}")
            exit()  # Exit the program
        else:  # Invalid input
            print(f"{RED}❌ Invalid input. Please enter 'y' for yes or 'n' for no.{RESET}")

# Main function to control the program flow
def main():
    """Main function to drive the program."""
    print_title()  # Print the program title

    while True:
        # Get user inputs for password length and number of passwords
        length = length_password()
        count = count_password()

        # Generate the requested number of passwords
        passwords = [generate_password(length) for _ in range(count)]

        # Display generated passwords
        print(f"\n{BLUE}Generated Passwords:{RESET}")
        for idx, pw in enumerate(passwords, 1):
            print(f"{GREEN}{idx}. {pw}{RESET}")
        
        # Ask if the user wants to save passwords
        save_passwords(passwords)
        
        # Ask if the user wants to generate more passwords
        generate_more_passwords()

# Run the program if this script is executed
if __name__ == "__main__":
    main()
