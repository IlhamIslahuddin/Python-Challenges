import random

letters = ["A","B","C","D","E","F"]
def generate_ipv4():
    address = ""
    for i in range (4):
        num = str(random.randint(1,255))
        address = address + num
        if i != 3:
            address = address + "."
    return address

def generate_ipv6():
    address = ""
    for j in range (8):
        for i in range (2):
            num = str(random.randint(0,9))
            letter = random.choice(letters)
            address = address + num + letter
        if j != 7:
            address = address + ":"
    return address

def ip_batch_generator():
    for i in range (50):
        ipv4 = generate_ipv4()
        print (ipv4)
    for i in range (50):
        ipv6 = generate_ipv6()
        print (ipv6)

if __name__ == "__main__":
    ip_batch_generator()
