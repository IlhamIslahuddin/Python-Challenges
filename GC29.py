import random

StudentNum = int(input("How many students? "))
StudentNames = ["Alex","Bobby","Chucky","Ducky","Eli","Freddy","Tom"]

GenericComments = ["- good job","- missing homework","- see me after class","- keep up the good work"]

for i in range(StudentNum):
  Report = random.choice(StudentNames)+random.choice(GenericComments)
  print(Report)
