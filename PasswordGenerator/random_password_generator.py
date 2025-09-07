import random
import string

## creating pool

pool = []
password = []
# Password length

Length = int(input("Enter password length 8 , 12 , 16: "))
# Include

lowercase = input("\nDo you want lowercase (a-z) in the password : ").lower().strip()
uppercase = input("\nDo you want Uppercase (A–Z) in the password : ").lower().strip()
numbers = input("\nDo you want Numbers (0-9) in the password : ").lower().strip()
symbol = input("\nDo you want Symbols (!@#$%^&*...) in the password : ").lower().strip()


if lowercase == "yes" or lowercase == "y":
    pool.extend("abcdefghijklmnopqrstuvwxyz")
    password.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
if uppercase == "yes" or uppercase == "y":
    pool.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    password.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
if numbers == "yes" or numbers == "y":
    pool.extend("0123456789")
    password.append(random.choice("0123456789"))
if symbol == "yes" or symbol == "y":
    pool.extend(string.punctuation)
    password.append(random.choice(string.punctuation))


if pool == []:
    print(
        "To generate a password, you must select at least one option (lowercase, uppercase, number, or symbol).\nPlease run the program again and enter 'yes' for at least one option."
    )
    exit()


for i in range(0, Length - len(password)):
    password.append(random.choice(pool))


random.shuffle(password)
print("\nPassword is : ", "".join(password))
