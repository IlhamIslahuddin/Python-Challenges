array_to_sort = [6,4,43,2,22,2,34,4,5]

def sort():
    temp = 0
    num_right = 0
    x = 0
    for i in range(99):
        if num_right >= len(array_to_sort)-1:
            break
        x += 1
        for j in range (len(array_to_sort)):
            if num_right >= len(array_to_sort)-1:
                break
            if j == len(array_to_sort) - 1:
                pass
            elif array_to_sort[j] > array_to_sort[j+1]:
                temp = array_to_sort[j]
                array_to_sort[j] = array_to_sort[j+1]
                array_to_sort[j+1] = temp
                num_right = 0
            else:
                num_right += 1
    print ("done after",x,"laps")
    print (array_to_sort)

sort()
