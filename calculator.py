def welcome():
    """This function displays a welcome message"""
    print("Welcome to Shecktar Calculator App")


def add(num1, num2):
    """This function adds two numbers"""
    return num1 + num2


def subtract(num1, num2):
    """This function subtracts two numbers"""
    return num1 - num2


def multiply(num1, num2):
    """This function multiplies two numbers"""
    return num1 * num2


def divide(num1, num2):
    """This function divides two numbers"""
    if num2 != 0:
        return num1 / num2
    else:
        print("Error: Division by zero is undefined")
        return None


def main():
    welcome()
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        operation = input("Enter choice (1/2/3/4): ")

        if operation in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid input. Please enter a number.")
                continue

            if operation == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif operation == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif operation == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif operation == '4':
                result = divide(num1, num2)
                if result is not None:
                    print(num1, "/", num2, "=", result)

            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break

        else:
            print("Invalid input")


# Call the main function
if __name__ == "__main__":
    main()
