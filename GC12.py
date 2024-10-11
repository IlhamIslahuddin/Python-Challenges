import time

def brotherly_screentime():
    valid = False
    while valid == False:
        try:
            my_time = int(input("How many minutes? "))
            valid = True
        except:
            print("Please input a whole number.")

    for x in range(my_time*60, 0, -1):
        seconds = x % 60
        minutes = int(x / 60)
        print(f"{minutes:02}:{seconds:02}")
        time.sleep(1)
    
    time.sleep(1)
    print ("Times up! Swap!")
    time.sleep(1)
    
    for x in range(my_time*60, 0, -1):
        seconds = x % 60
        minutes = int(x / 60)
        print(f"{minutes:02}:{seconds:02}")
        time.sleep(1)
        
    print ("Times up!")

if __name__ == "__main__":
    brotherly_screentime()
