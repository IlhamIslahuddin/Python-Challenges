count = 0
my_byte = str(input("Input your byte: "))
for i in my_byte:
    if i == "1":
      count = count +1
print(count)

if count%2 == 0:
  print ("Even number of 1s")
elif count%2 ==1:
  print ("Odd number of 1s")
