num = int(input("what numbers times table would you like? "))
limit = int(input("up to what number? "))

for i in range (limit):
  print (num, "x", i+1, "=", num*(i+1))
