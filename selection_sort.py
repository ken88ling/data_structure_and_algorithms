def selection_sort(arr):
    n = len(arr)

    # Traverse through all list elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted list
        min_idx = i
        for j in range(i + 1, n):
            print(f"i = {i}")
            if arr[j] < arr[min_idx]:
                print(f" j = {j}")
                min_idx = j

        # Swap the found minimum element with the first element of the unsorted list
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Test the function
arr = [64, 25, 12, 22, 11]
print("Original list:", arr)
selection_sort(arr)
print("Sorted list:", arr)
