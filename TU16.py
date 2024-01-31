ringgit = float(input("how much ringgit? "))
print (f"RM{ringgit}")

number = int(input("what is the denary number? "))
print(f"Binary:{number:b}")

listofnumbers = [13,2314,1321,44535,436,4353,3423,2]

print("\nNumber Table")
for i in range(len(listofnumbers)-3):
    print(f"{listofnumbers[i]}   {listofnumbers[i+1]}   {listofnumbers[i+2]}   {listofnumbers[i+3]}")
