import random

mynumber = random.randint(0,100)
#print (mynumber)

myfloat = random.uniform(0.1,9.9)
#print (myfloat)


for i in range(8):
  NamePicker = ["John","James","Alex","Alan","Bobby","Timmy","Tom"]
  print (NamePicker)
  PickedName = random.choice(NamePicker)
  print (PickedName)  
  
  x = int(input("Do you want to remove this name from the list? (1=yes) "))
  if (x == 1):
    NamePicker.remove(PickedName)
    print (PickedName,"has been removed from the list")
    print (NamePicker)
    break
  else:
    print (PickedName,"has not been removed from the list")
    print (NamePicker)
    break
