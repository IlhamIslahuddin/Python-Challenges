def num_vowels():
    vowels = ["a","e","i","o","u"]
    InString = str(input("Input text: "))
    vowel_count = 0
    for i in range (len(InString)):
        if InString[i].lower() in vowels:
            vowel_count += 1
    print ("Number of vowels in the text: ",vowel_count)
    return vowel_count

if __name__ == "__main__":
    num_vowels()
