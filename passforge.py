# ===== Advanced Password Generator =====

# Import required modules
import string
import random

# Function to display the program title
def print_title():
    print("\033[1;31m[+] ====== Welcome to Advanced Password Generator ====== [+]\033[0m")

# Function to ask for password length
def length_password():
    while True:
        try:
            length = int(input("How many characters should the password have? (8–65): "))
            if length < 8:
                print("Password must be at least 8 characters long.")
            elif length > 65:
                print("Password must be 64 characters or less.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to ask how many passwords to generate
def count_password():
    while True:
        try:
            count = int(input("How many passwords would you like to generate?: "))
            if count < 1:
                print("Please enter a number greater than 0.")
            else:
                return count
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to generate a single password
def generate_password(length):
    password = []

    # Character sets
    lower_chars = list(string.ascii_lowercase)
    upper_chars = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    # Shuffle character sets for randomness
    random.shuffle(lower_chars)
    random.shuffle(upper_chars)
    random.shuffle(digits)
    random.shuffle(punctuation)

    # Estimate how many characters to use from each set
    lower_upper_count = round(length * 0.4)  # 40% lowercase & uppercase
    digit_punct_count = round(length * 0.1)  # 10% digits & punctuation

    # Add lowercase and uppercase characters
    for i in range(lower_upper_count):
        password.append(lower_chars[i % len(lower_chars)])
        password.append(upper_chars[i % len(upper_chars)])

    # Add digits and punctuation characters
    for i in range(digit_punct_count):
        password.append(digits[i % len(digits)])
        password.append(punctuation[i % len(punctuation)])

    # Fill remaining characters randomly if needed
    while len(password) < length:
        password.append(random.choice(
            lower_chars + upper_chars + digits + punctuation
        ))

    # Final shuffle for complete randomness
    random.shuffle(password)
    return ''.join(password[:length])

# Main function
def main():
    print_title()

    while True:
        length = length_password()
        count = count_password()

        print("\nGenerated Passwords:")
        for i in range(count):
            password = generate_password(length)
            print(f"{i + 1}. {password}")

        # Ask if user wants to generate more passwords
        while True:
            repeat = input("\nGenerate more passwords? [Y/n]: ").strip().lower()
            if repeat == "y" or repeat == "":
                break
            elif repeat == "n":
                print("Thank you for using the Advanced Password Generator. Goodbye!")
                exit()
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")

# Run the program
if __name__ == "__main__":
    main()
