from playsound import playsound
import time

# Clear whole console
CLEAR = "\033[2J"
CLEARANDRETURN = "\033[H"

def alarm(seconds) :
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f'{CLEARANDRETURN}Alarm will sound in : {minutes_left:02d} : {seconds_left:02d}')

    print(CLEARANDRETURN)
    print("Time Over !!")
    playsound("C:\Users\Aman\Documents\sample.mp3")

print("Program to set timer and play alarm sound when time is over")
hours = int(input("Eneter Hours : "))
minutes = int(input("Enter minutes : "))
seconds = int(input("Enter seconds : "))
total_seconds = int((minutes * 60) + seconds)
alarm(total_seconds)
