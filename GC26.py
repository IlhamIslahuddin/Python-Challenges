def drunkometer(text):
    initial = text
    attempt = ""
    print ("the initial text is:",initial)
    for i in range (2):
        attempt = input("type the initial text: ")
        if attempt != initial:
            break
    if attempt == initial:
        print ("passed")
        return False
    else:
        print ("failed")
        return True

if __name__ == "__main__":
    drunkometer("akpiftxdg")
