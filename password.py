import random
import string
import re
import pyperclip  


def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    number_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    strength = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if strength == 8:
        return "Strong Password "
    elif strength >= 4:
        return "Medium Password "
    else:
        return "Weak Password "


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    characters = []
    guaranteed_chars = []  

    if use_uppercase:
        characters.extend(string.ascii_uppercase)
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        characters.extend(string.ascii_lowercase)
        guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if use_numbers:
        characters.extend(string.digits)
        guaranteed_chars.append(random.choice(string.digits))
    if use_special:
        characters.extend(string.punctuation)
        guaranteed_chars.append(random.choice(string.punctuation))

    if not characters:
        return "Error: You must select at least one character type!"

   
    password = guaranteed_chars + [random.choice(characters) for _ in range(length - len(guaranteed_chars))]
    random.shuffle(password)  
    return ''.join(password)  


length = int(input("Enter the desired password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'


use_custom_password = input("Do you want to enter your own password? (y/n): ").lower() == 'y'

if use_custom_password:
    password = input("Enter your custom password: ")
else:
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)


print(f"\nYour Password: {password}")
print(check_password_strength(password))


pyperclip.copy(password)
print("\nPassword copied to clipboard! ")
