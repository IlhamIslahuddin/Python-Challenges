input1 = int
input2 = int

def NAND(input1,input2):
    # if input1 != 0 and input1 != 1:
    #     print ("Invalid input")
    #     return -1
    # elif input2 != 0 and input2 != 1:
    #     print ("Invalid input")
    if input1 == 1 and input2 == 1:
        return 0
    else:
        return 1

def OR(input1,input2):
    if NAND(input1,input2) == 0:
        return 1
    if NAND(1,input2) == 0 or NAND(input1,1) == 0:
        return 1
    else:
        return 0
    
def AND(input1,input2):
    if NAND(input1,input2) == 1:
        return 0
    else:
        return 1
    
def NOT(input1):
    if NAND(input1,input1) == 1:
        return 1
    else:
        return 0
    
def XOR(input1,input2):
    if NAND(input1,input2) == 0:
        return 0
    if NAND(1,input2) == 0 and NAND(input1,1) == 0:
        return 0
    elif NAND(1,input2) != 0 and NAND(input1,1) == 0:
        return 1
    elif NAND(1,input2) == 0 and NAND(input1,1) != 0:
        return 1
    else:
        return 0
    
def NOR(input1,input2):
    if NAND(input1,input2) == 0:
        return 0
    if NAND(1,input2) == 0 or NAND(input1,1) == 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    nor = NOR(0,0)
    orx = OR(0,0)
    xor = XOR(0,0)
    andx = AND(0,0)
    notx = NOT(0)    
    nand = NAND(0,0)

    print ("nor",nor)
    print ("or",orx)
    print ("xor",xor)
    print ("and",andx)
    print ("not",notx)
    print ("nand",nand)
