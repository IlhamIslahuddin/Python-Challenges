import time

def timer():
    minutes = int(input("How many minutes? "))
    seconds = minutes * 60
    while seconds != 0:
        mins, secs = divmod(seconds, 60)
        timer_display = '{:02d}:{:02d}'.format(mins, secs)
        print(timer_display, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

if __name__ == "__main__":
    timer()
