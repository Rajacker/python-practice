def print_pyramid(height):
    # Loop through each level of the pyramid
    for i in range(height):
        # Print spaces before the stars
        for j in range(height - i - 1):
            print(" ", end="")
        # Print stars
        for k in range(2 * i + 1):
            print("*", end="")
        # Move to the next line
        print()

# Get the height of the pyramid from the user
try:
    height = int(input("Enter the height of the pyramid: "))
    print_pyramid(height)
except ValueError:
    print("Please enter a valid integer for the height.")
