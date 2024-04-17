def first_and_last():
    array = [7,3,4,5,4342,2,233,54,5,12,3,33,5,6,7,9,9,8,77,9,9,7,7,5]
    newarray = []
    first = array[0]
    newarray.append(first)
    last = array[len(array)-1]
    newarray.append(last)
    print ("first element of the array: ",first)
    print ("last element of the array: ",last)
    print ("new list: ",newarray)
    

if __name__ == "__main__":
    first_and_last()
