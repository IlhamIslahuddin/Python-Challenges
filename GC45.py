input = str(input("please input only one character so this variable can be classed as char: "))

if len(input) > 1 or len(input) == 0 or type(input) == 'int':
  print ("not a char")
else:
  print ("char")
