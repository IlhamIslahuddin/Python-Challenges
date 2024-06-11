def minimum_difference(arr):
    arr.sort()
    
    # Initialize minimum difference with a large value
    min_diff = float('inf')
    
    # Iterate through the array and compare adjacent elements
    for i in range(len(arr) - 1):
        diff = arr[i+1] - arr[i]
        # Update min_diff if the current difference is smaller
        if diff < min_diff:
            min_diff = diff
            
    return min_diff

if __name__ == "__main__":
    numbers = [1, 5, 3, 9,27,32,1.5]
    print("Minimum difference between two numbers in the array:", minimum_difference(numbers))
