# Define a function called mystery with two parameters: n and m
def mystery(n, m):
    # Check if n is equal to 0
    if n == 0:
        # If n is 0, return the value of m
        return m
    else:
        # If n is not 0, call mystery recursively with n-1 and add 1 to the result
        result = mystery(n - 1, m) + 1
        # Print the intermediate result (optional)
        print(f"mystery({n}, {m}) = {result}")
        # Return the result
        return result


# Example usage:
n = 4
m = 5
result = mystery(n, m)
print(f"Final result: mystery({n}, {m}) = {result}")
