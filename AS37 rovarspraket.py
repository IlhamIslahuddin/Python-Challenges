#only supports lowercase text

def rovarspraket():
    initial_text = str(input("Input text: "))
    rovarspraket = ""
    consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    for i in range(len(initial_text)):
        if initial_text[i] in consonants:
            adding = str(initial_text[i]) + "o" + str(initial_text[i])
            rovarspraket = rovarspraket + str(adding)
        else:
            rovarspraket = str(rovarspraket) + str(initial_text[i])
    print (rovarspraket)

if __name__ == "__main__":
    rovarspraket()
