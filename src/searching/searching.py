def linear_search(arr, target):
    # Your code here
    for i, val in enumerate(arr):
        if val == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1
    found = False

    while end >= start and not found:
        middle = (start + end) // 2

        if arr[middle] == target:
            found = True
            return middle

        else:
            if target < arr[middle]:
                end = middle - 1
            if target > arr[middle]:
                start = middle + 1

    return -1  # not found
