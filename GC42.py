import random

def random_number_list():
    initial = random.randint(0,10000)
    list = [initial]
    total = initial
    min = initial
    max = initial
    for i in range(99):
        new = random.randint(0,10000)
        if new > max:
            max = new
        if new < min:
            min = new
        total += new
        list.append(new)
    print ("Minimum: ",min)
    print ("Maximum: ",max)
    average = total / 100
    print ("Mean: ",average)
    print ("List: ",list)

if __name__ == "__main__":
    random_number_list()
