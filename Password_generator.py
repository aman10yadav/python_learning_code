import random
import string

def generatePassword(minLength, number=True, specialCharacters=True):
    '''print(min_length)
    print(number)
    print(special_characters) '''

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    #print(letters, digits, symbols)

    characters = letters
    if number == True:
        characters += digits

    if specialCharacters == True:
        characters += symbols
    
    #print(characters)

    password = ""
    meetsCriteria = False
    hasDigits = False
    hasSymbols = False

    while not meetsCriteria or len(password) < minLength:
        newCharacter = random.choice(characters)
        password += newCharacter

        if newCharacter in symbols:
            hasSymbols = True
        elif newCharacter in digits :
            hasDigits = True

        meetsCriteria = True
        if number :
            meetsCriteria = hasDigits
        if specialCharacters :
            meetsCriteria = meetsCriteria and hasSymbols

    return password


minLength = int(input("Enter length of password you want : "))
number = input("Do you want numbers in password? (y/n) : ").lower() == 'y'
symbols = input("Do you want symbols in password? (y/n) : ").lower() == 'y'
password = generatePassword(minLength, number, symbols)
print(password)
