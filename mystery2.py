def sum_list(A, n):
    # Check if n is equal to 0
    if n == 0:
        # If n is 0, return 0 (base case)
        return 0
    else:
        # If n is not 0, calculate the sum recursively for n-1 elements and add A[n-1]
        # result = sum_list(A, n - 1) + A[n - 1]
        result = sum_list(A, n - 1) + A[n - 1]
        # Print the intermediate result (optional)
        print(f"sum_list({A}, {n}) = {result}")
        # Return the result
        return result


# Example usage:
A = [4, 3, 6, 2, 5]
n = 5


result = sum_list(A, n)
print(f"Final result: sum_list({A}, {n}) = {result}")
