num1 = int(input("First digit: "))
num2 = int(input("Second digit: "))
num3 = int(input("Third digit: "))
num4 = int(input("Fourth digit: "))
check_digit = int(input("Check digit: "))

num1 = num1*5
num2 = num2*4
num3 = num3*3
num4 = num4*2

total = num1 + num2 + num3 + num4

mod = total % 11
if 11 - mod == check_digit:
  print ("checksum is valid")
else:
  print ("checksum is invalid")
