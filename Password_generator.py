import string
import random

# Function to generate a password with optional numbers and special characters
def generate_password(minimum_length,numbers=True,special_charachters=True):

    # Define character sets
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    # Build the allowed character set based on user preferences
    characters=letters
    if numbers:
        characters+=digits
    if special_charachters:
        characters+=special    

    # Initialize password and criteria flags
    password=''
    meets_criteria=False
    has_numbers=False
    has_special=False

     # Generate password until it meets conditions and reaches the required length
    while not meets_criteria or len(password)<minimum_length:

        new_character=random.choice(characters)
        password+=new_character

        if new_character in digits:
            has_numbers=True

        elif new_character in special:
            has_special=True   

        # Ensure password meets character requirements
        meets_criteria=True
        if numbers:
            meets_criteria=has_numbers
        if special_charachters:
            meets_criteria=meets_criteria and has_special

    return password

# Get user input for password preferences
min_length = int(input("Enter the minimum length of password you want."))
numbers = input("Do you want to include numbers (y/n)").lower()=='y'
special_characters = input("Do you want to include Special characters (y/n)").lower()=='y'

# Generate and display the password
pwd=generate_password(min_length,numbers,special_characters)
print(pwd)
                     