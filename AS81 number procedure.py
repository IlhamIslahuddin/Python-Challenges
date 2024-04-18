def number_procedure():
    sum = 0
    product = 1
    list_of_nums = [1,4,5,23,5,2]
    for i in range (len(list_of_nums)):
        sum += list_of_nums[i]
        product = product*list_of_nums[i]
    print ("list: ",list_of_nums)
    print ("amount of numbers: ",len(list_of_nums))
    print ("sum: ",sum)
    print ("product: ",product)

if __name__ == "__main__":
    number_procedure()
