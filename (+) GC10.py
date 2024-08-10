def print_fibonacci_sequence(num_terms):
    a = 0
    b = 1
    for _ in range(num_terms):
        print(a, end=' \n',)
        a, b = b, a + b #calculation carried out simultaneously

if __name__ == "__main__":
    print_fibonacci_sequence(100) 
