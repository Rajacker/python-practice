def calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Error! Division by zero."

    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in operations:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = operations[choice](num1, num2)
            print(f"The result is: {result}")
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

# Run the calculator function
calculator()
