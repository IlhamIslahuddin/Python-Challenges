def make_it_laugh():
    string = str(input("Initial string: "))
    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    laugh_string = ""
    for i in range (len(string)):
        if string[i] in vowels:
            laugh_string = laugh_string + "haha"
        else:
            laugh_string = laugh_string + string[i]
    print ("Modified string: ",laugh_string)
    
if __name__ == "__main__":
    make_it_laugh()
