GivenNumber = int(input("Insert integer number: "))
if (GivenNumber % 3) == 0:
  print ("yes your number can be divided by 3 without remainders")
if (GivenNumber % 3) != 0:
  print ("no your number cannot be divided by 3 without remainders")
  print ("the remainder is: ",GivenNumber % 3)
