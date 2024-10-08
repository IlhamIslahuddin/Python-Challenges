# A223 NEAT FROM 101 TO 1000

def neat_numbers():
    for i in range (101,1001):
        string = str(i)
        total = 0
        for char in string:
            num = int(char)
            total += num
        if i % total == 0:
            print (f"{i} is neat")

if __name__ == "__main__":
    neat_numbers()
