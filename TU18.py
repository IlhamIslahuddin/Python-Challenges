#reads seperate text files which contain poems called "Rudyard" and "Mam:

import time

def poem_read():  
    choice = int(input("Would you like to read Rudyard (1) or Mam (2)? "))

    if choice == 1:
        with open("rudyard.txt","r") as whole_file:
            print ("Now reading: Rudyard")
            for line in whole_file:
                time.sleep(3)
                print(line,end="")
    elif choice == 2:
        with open("mam.txt","r") as whole_file:
            print ("Now reading: Mam")
            for line in whole_file:
                time.sleep(3)
                print(line,end="")
    else:
        print ("Unrecognised input.")

if __name__ == "__main__":
    poem_read()
