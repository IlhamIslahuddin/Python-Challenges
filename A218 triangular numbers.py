def trianglular_nums():
    n = int(input("How many triangular numbers? "))
    for i in range (n):
        num = 1/2*(i+1)*(i+2)
        print (int(num))

if __name__ == "__main__":
    trianglular_nums()
