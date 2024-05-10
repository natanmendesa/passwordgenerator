from string import *
from random import *

def passwordgen(length: int, arg1: bool, arg2: bool):
    passwords = []
    password = ""

    if arg1 == True and arg2 == True:
        for i in range(length):
            letters_digits_specials = ascii_letters + digits + punctuation

            number = randint(0, len(letters_digits_specials) - 1)

            password += letters_digits_specials[number]
    
        passwords.append(password)
    elif arg1 == True and arg2 == False:
        for i in range(length):
            letters_digits = ascii_letters + digits

            number = randint(0, len(letters_digits) - 1)

            password += letters_digits[number]

        passwords.append(password)
    elif arg1 == False and arg2 == True:
        for i in range(length):
            letters_specials = ascii_letters + punctuation

            number = randint(0, len(letters_specials) - 1)

            password += letters_specials[number]

        passwords.append(password)
    else:
        for i in range(length):
            letters = ascii_letters

            number = randint(0, len(letters) - 1)

            password += letters[number]

    
        passwords.append(password)



    return passwords

for i in range(10):
    print(passwordgen(8, True, False))




