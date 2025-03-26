from playsound import playsound  # Importing playsound to play the alarm sound
import time   # Importing time module for countdown functionality

# Escape sequences for clearing the console screen
Clear='\033[2J'
Clear_And_Return='\033[H'

# Function to set and run the alarm
def alarm(seconds):
    time_elapsed=0

    print(Clear)    # Clearing the screen before starting the countdown
    while time_elapsed<seconds:
        time.sleep(1)   # Pausing for one second in each iteration
        time_elapsed+=1

        # Calculating remaining time
        time_left=seconds-time_elapsed
        minutes_left=time_left // 60
        seconds_left=time_left % 60

        # Displaying the countdown timer
        print(f"{Clear_And_Return}Your alarm will sound in:{minutes_left:02d}:{seconds_left:02d}")

    playsound('alarm.mp3')    # Playing the alarm sound when the timer reaches zero

# Taking user input for the alarm duration
minutes=int(input("For how many minutes you want to set the alarm"))
seconds=int(input("For how many seconds you want to set the alarm"))
timer=minutes*60+seconds

alarm(timer)  # Starting the alarm countdown