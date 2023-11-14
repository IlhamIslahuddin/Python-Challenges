MyHeight = 172
TheirHeight = int(input("What is your height in cm?: "))
if TheirHeight < MyHeight:
  print ("I am", (MyHeight - TheirHeight), "cm taller than you")
if TheirHeight > MyHeight:
  print ("Wow! You are", (TheirHeight - MyHeight),"cm taller than me!")
if TheirHeight == MyHeight:
  print ("We are the same height!")
