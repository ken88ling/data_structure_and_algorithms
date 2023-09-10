# Global variable to count function calls
call_count = 0


def Fibo(n):
    # Declare the call_count variable as global
    global call_count

    if n == 1 or n == 2:
        return 1

    # Increment the call_count each time the function is called
    call_count += 1

    result = Fibo(n - 1) + Fibo(n - 2)
    print(f"Fibo {result}")
    return result


# Example usage:
n = 13
result = Fibo(n)
print(f"Final result: Fibo({n}) = {result}")
print(f"Function was called {call_count} times.")
