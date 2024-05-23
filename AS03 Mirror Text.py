def mirrortext():
    original = input("Input text to be mirrored: ")
    mirrored = ""
    for i in range (len(original),0,-1):
        mirrored = mirrored + original[i-1]
    print ("Mirrored text: ",mirrored)
        
if __name__ == "__main__":
    mirrortext()
