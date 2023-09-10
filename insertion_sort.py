def insertion_sort(arr):
    n = len(arr)

    # Traverse through 1 to len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        print(f"Key to insert: {key}")

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            print(f"Moved {arr[j]} to position {j+1}: {arr}")
            j -= 1

        arr[j + 1] = key
        print(f"Inserted key {key} at position {j+1}: {arr}")
        print("----")

    return arr


# Test the function
arr = [64, 25, 12, 22, 11]
print("Original list:", arr)
insertion_sort(arr)
print("Sorted list:", arr)
