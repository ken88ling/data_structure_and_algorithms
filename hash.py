def example(n):
    if n > 0:
        example(n // 2)  # Recursive call 1, using integer division (//)
        example(n // 2)  # Recursive call 2, using integer division (//)

    print("#")  # Output a "#" character without a newline


# Example usage:
n = 5  # Replace with your desired number
example(n)
