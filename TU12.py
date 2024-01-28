MyList = [1,2,3,4,5,6]

print (*MyList[0:4],sep=",")


VGChars = ["Mario","Luigi","Peach","Daisy","Bowser","Wario"]
VGChars.sort()
print (*VGChars,sep=",")

NewChar = input("What character would you like to add? ")
VGChars.append(NewChar)
print (VGChars)
