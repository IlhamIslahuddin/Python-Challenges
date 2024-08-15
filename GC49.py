import random
import time
def primary_quiz_machine():
    timer = int(input("How many seconds would you like to have before the answer appears? "))
    max_digits = int(input("What is the maximum number of digits you would like to work with? "))
    operations = ["+","-","/","X"]
    points = 0
    answer = 0
    user_ans = 0
    winning = True
    while winning == True:
        num1 = random.randint(0,((10**max_digits) - 1))
        num2 = random.randint(0,((10**max_digits) - 1))
        operation = random.choice(operations)
        print ("Question: ",num1,operation,num2)
        time.sleep(timer)
        user_ans = (input("Times up! What is the answer? \n"))
        if operation == "+":
            answer = num1 + num2
        elif operation == "-":
            answer = num1 - num2
        elif operation == "/":
            answer = num1 / num2
        elif operation == "X":
            answer = num1 * num2
        if float(user_ans) == float(answer):
            points += 1
            print (f"Correct! You currently have {points} points!")
        else:
            print (f"Incorrect. The correct answer was {answer}. \nGame over. You ended with {points} points")
            winning = False
    
if __name__ == "__main__":
    primary_quiz_machine()
