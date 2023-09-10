def bubble_sort(arr):
    n = len(arr)

    # Traverse through all list elements
    for i in range(n):
        print(f"Starting pass {i+1}")
        swapped = False

        # Last i elements are already in place, no need to check them
        for j in range(0, n - i - 1):
            # Traverse the list from 0 to n-i-1. Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"Swapped {arr[j+1]} with {arr[j]}: {arr}")
                swapped = True
            else:
                print(f"No swap needed for {arr[j]} and {arr[j+1]}")

        # If no two elements were swapped in the inner loop, the list is sorted
        if not swapped:
            print("No swaps occurred this pass. List is sorted.")
            break

    return arr


# Test the function
arr = [64, 25, 12, 22, 11]
print("Original list:", arr)
bubble_sort(arr)
print("Sorted list:", arr)
