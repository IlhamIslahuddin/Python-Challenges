import random
number = random.randint(1,100)
guess = int(input("guess the number from 1-100: "))

while guess != number:
    if guess > number:
        print("lower")
    elif guess < number:
        print("higher")
    guess = int(input("guess the number from 1-100: "))

print ("correct!")
