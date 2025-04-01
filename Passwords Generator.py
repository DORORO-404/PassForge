# import modules
import string
import random
print("----------Welcome To Password Generator----------")
while True:
# store all characters in list
    string_1 = list(string.ascii_lowercase)
    string_2 = list(string.ascii_uppercase)
    string_3 = list(string.digits)
    string_4 = list(string.punctuation)

    # shuffle all lists
    random.shuffle(string_1)
    random.shuffle(string_2)
    random.shuffle(string_3)
    random.shuffle(string_4)

# make sure the number of characters is 6 or more
    while True:
        try:
            characters_number = int(input("how many characters for the password?: "))
            if characters_number <8 :
                print("you need at least 8 characters")
            else:
                break
        except:
            print("please entre number only")

# calculate 40% and 10% of number of characters
    part_1 = round(characters_number * (40/100))
    part_2 = round(characters_number * (10/100))

# generate password
    password = []

    for row in range(part_1):
        password.append(string_1[row])
        password.append(string_2[row])

    for row in range(part_2):
        password.append(string_3[row])
        password.append(string_4[row])

# finally print password
    random.shuffle(password)
    password = "".join((password[0:]))
    print(password)

# Ask the user if they want to perform another operation
    while True:
        ask_user = input("Do you want to perform another operation? [Y/n]: ").strip().lower()
        if ask_user == "y":
            break
        elif ask_user == "n":
            print("Program exited.")
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            