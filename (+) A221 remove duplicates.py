def remove_duplicates(input_list):
    seen = set()
    unique_list = []
    for item in input_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

if __name__ == "__main__":
    original_list = [1,2,2,"twelve",2,"twelve",3,3,4,5,6,6,6,6]
    print (remove_duplicates(original_list))
