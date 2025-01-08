def only_whole_numbers():
    valid = False
    while valid == False:
        try:
            num = int(input("Input whole number: "))
            valid = True
        except:
            pass
        
if __name__ == "__main__":
    only_whole_numbers()
