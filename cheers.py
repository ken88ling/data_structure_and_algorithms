def cheers(times):
    if times > 0:
        print("Hip")  # Output "Hip"
        cheers(times - 1)  # Recursive call with times - 1

    print("Hooray")  # Output "Hooray"


# Example usage:
times = 1  # Replace with your desired number of cheers
cheers(times)
