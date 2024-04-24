def word_merge():
    word1 = str(input("What is the first string? "))
    word2 = str(input("What is the second string? "))
    merged = ""
    x = len(word1)
    y = len(word2)
    if x > y:
        First = True
    else:
        First = False
    if First == True:
        for i in range (y):
            merged = merged + word1[i]
            merged = merged + word2[i]             
    else:
        for i in range (x):
            merged = merged + word1[i]
            merged = merged + word2[i]
            
    if First == True:
        for i in range (y,(x-y)+y):
            merged = merged + word1[i]
    else:
        for i in range (x,(y-x)+x):
            merged = merged + word1[i]

    return print(merged)
    

if __name__ == "__main__":
    word_merge()
