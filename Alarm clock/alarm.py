from playsound import playsound
import time

Clear='\033[2J'
Clear_And_Return='\033[H'

def alarm(seconds):
    time_elapsed=0

    print(Clear)
    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed+=1

        time_left=seconds-time_elapsed
        minutes_left=time_left // 60
        seconds_left=time_left % 60

        print(f"{Clear_And_Return}Your alarm will sound in:{minutes_left:02d}:{seconds_left:02d}")

    playsound('alarm.mp3')    
minutes=int(input("For how many minutes you want to set the alarm"))
seconds=int(input("For how many seconds you want to set the alarm"))
timer=minutes*60+seconds

alarm(timer)        