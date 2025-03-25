import random # Importing the random module to generate random numbers

# Taking user input for the top limit of the range and handling invalid inputs
try:
    top_of_range = int(input("Enter a number that will be your top of range: "))  # Try converting input to an integer
    if top_of_range <= 0:
        print('Please enter a number greater than 0 next time.')
        quit()
except ValueError:
    print("Please enter a valid number next time.")
    quit()

# Generating a random number within the user-specified range
random_number=random.randint(0,top_of_range)
guesses=0
# Loop for user to guess the number until the correct guess
while True:
    guesses +=1
    try:
        user_guess=int(input("Enter your guess"))
    except ValueError:
        print("Please enter a valid number next time.")
        continue
    # Checking if the guess is correct, too high, or too low
    if user_guess==random_number:
        print("You got it right !")
        break
    elif user_guess>random_number:
        print("wrong! your guess is above the number")
    else:
        print("wrong! your guess is below the number")
# Displaying the total number of attempts
print("you guesseed it in",guesses,"guesses")

