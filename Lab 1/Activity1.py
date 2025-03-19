def find_second_largest_smallest(arr):
    if len(arr) < 2:
        return None, None
    unique_arr = list(set(arr))
    if len(unique_arr) < 2:
        return None, None
    unique_arr.sort()
    second_smallest = unique_arr[1]
    print("second smallest number:",second_smallest)
    second_largest = unique_arr[-2]
    print("second largest number:",second_largest)
    return second_largest, second_smallest
arr = [12,55,32,678,89]
print(find_second_largest_smallest(arr))
