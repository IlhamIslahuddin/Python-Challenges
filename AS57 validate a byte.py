def even_parity_check():
    byte = str(input("Enter Byte: "))
    parity = 0
    if len(byte) != 8:
        statement = "invalid length of byte"
        return print(statement)
    for i in range (len(byte)):
        if byte[i] == "1":
            parity += 1
        elif byte[i]  == "0":
            pass
        else:
            statement = ("invalid character detected")
            return print(statement)
    if parity % 2 == 0:
        print ("even parity passed")
    else:
        print ("even parity failed")

if __name__ == "__main__":
    even_parity_check()
