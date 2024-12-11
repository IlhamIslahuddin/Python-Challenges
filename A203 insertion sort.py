def insertion_sort(list):
    for i in range(1, len(list)):
        position = i
        current_value = list[position]
        while position > 0 and list[position - 1] > current_value:
            buffer = list[position - 1]
            list[position - 1] = current_value
            list[position] = buffer
            position -= 1
    return (list)


if __name__ == "__main__":
    array = [1,3,9,6,2,5,4,8,7]
    ans = insertion_sort(array)
    print(ans)
