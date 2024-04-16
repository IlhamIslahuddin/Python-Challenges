def linearsearch():
    array_to_search = ["alpha","beta","charlie","delta","echo","foxtrot","golf","hotel","india","juliet","kilo","lima","mike","november","oscar","papa","quebec","romeo","sierra","tango","uniform","victor","whiskey","x-ray","yankee","zulu"]
    word_search = input("input word: ")
    Found = False
    for i in range(len(array_to_search)):
        if array_to_search[i] == word_search:
            print ("found at index",i,"of the array")
            Found = True
            break
    if Found == False:
        print ("your word was not in the array")
