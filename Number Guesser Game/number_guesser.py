import random

try:
    top_of_range = int(input("Enter a number that will be your top of range: "))  # Try converting input to an integer
    if top_of_range <= 0:
        print('Please enter a number greater than 0 next time.')
        quit()
except ValueError:
    print("Please enter a valid number next time.")
    quit()

random_number=random.randint(0,top_of_range)
guesses=0
while True:
    guesses +=1
    try:
        user_guess=int(input("Enter your guess"))
    except ValueError:
        print("Please enter a valid number next time.")
        continue

    if user_guess==random_number:
        print("You got it right !")
        break
    elif user_guess>random_number:
        print("wrong! your guess is above the number")
    else:
        print("wrong! your guess is below the number")

print("you guesseed it in",guesses,"guesses")

