# import modules
import string
import random

print("----------Welcome To Password Generator----------")

while True:
    # Reset password list for each generation
    password = []

    # store all characters in list
    lower_chars = list(string.ascii_lowercase)
    upper_chars = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    # shuffle all lists
    random.shuffle(lower_chars)
    random.shuffle(upper_chars)
    random.shuffle(digits)
    random.shuffle(punctuation)

    # make sure the number of characters is 6 or more
    while True:
        try:
            length = int(input("How many characters for the password? (minimum 8): "))
            if length <8 :
                print("Password must be at least 8 characters long.")
            else:
                break
        except:
            print("Please enter a valid number.")

    # calculate 30% and 20% of number of characters
    part_1 = round(length * (30/100)) 
    part_2 = round(length * (20/100))

    # generate password
    for row in range(part_1):
        password.append(lower_chars[row])
        password.append(upper_chars[row])

    for row in range(part_2):
        password.append(digits[row])
        password.append(punctuation[row])

    # finally print password
    random.shuffle(password)
    password = "".join((password[0:]))
    print(password)

    # Ask the user if they want to perform another operation
    while True:
        repeat = input("Generate another password? [Y/n]: ").strip().lower()
        if repeat == "y":
            break
        elif repeat == "n":
            print("Thank you for using the Password Generator. Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter 'Y' or 'n'.")
