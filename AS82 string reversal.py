def reverse_string():
    string = str(input("Input string: "))
    reversed = ""
    x = len(string)
    for i in range (x):
        reversed = reversed + string[x-1-i]
    print ("reversed string: ",reversed)
    return (reversed)
    
if __name__ == "__main__":
    reverse_string()
