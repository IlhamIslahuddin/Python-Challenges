import random

def binary_search(lowest, highest):
    success = False
    middle = (lowest + highest) // 2
    random_num = random.randint(lowest, highest)
    while success == False:
        if random_num == middle:
            print (f"the number is {random_num}")
            success = True
        elif random_num > middle:
            lowest = middle
            middle = int((lowest + highest) / 2)
            print ("num guessed was too large")
        elif random_num < middle:
            highest = middle
            middle = int((lowest + highest) / 2)
            print ("num guessed was too small")
    
if __name__ == "__main__":
    binary_search(1,111)
