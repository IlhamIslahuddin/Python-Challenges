def stair_pyramid():
    size = int(input("Input size of pyramid: "))
    stairs = 1
    for i in range (size):
        print ("x"*stairs)
        stairs += 2

if __name__ == "__main__":
    stair_pyramid()
