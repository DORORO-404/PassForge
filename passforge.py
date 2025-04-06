# import modules
import string
import random

print("\033[1;31m[+] ====== Welcome To Advanced Password Generator ====== [+]\033[0m")

while True:
    # Reset password list for each generation
    password = []

    # Character sets
    lower_chars = list(string.ascii_lowercase)
    upper_chars = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    # Shuffle all sets
    random.shuffle(lower_chars)
    random.shuffle(upper_chars)
    random.shuffle(digits)
    random.shuffle(punctuation)

    # Get password length with validation
    while True:
        try:
            length = int(input("How many characters for the password?: "))
            if length <8 :
                print("Password must be at least 8 characters long.")
            elif length > 65:
                print("Password must be less than 65 characters long.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Calculate character distribution
    partie_1 = round(length * (40/100)) 
    partie_2 = round(length * (10/100))

    # generate password
    for row in range(partie_1):
        password.append(lower_chars[row])
        password.append(upper_chars[row])

    for row in range(partie_2):
        password.append(digits[row])
        password.append(punctuation[row])

    # Shuffle and display password
    random.shuffle(password)
    final_password = "".join(password)
    print(f"Generated Password: \"{final_password}\"")

    # Ask to continue
    while True:
        repeat = input("Generate another password? [Y/n]: ").strip().lower()
        if repeat == "y":
            break
        elif repeat == "n":
            print("Thank you for using the Password Generator. Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
