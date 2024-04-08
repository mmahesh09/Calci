import math

def calculator():
    print("Welcome to Simple Calculator!")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Logarithm (log)")
    print("6. Trigonometric Functions (sin, cos, tan)")
    print("7. Inverse Trigonometric Functions (asin, acos, atan)")
    print("Enter 'quit' to exit")

    while True:
        operation = input("Enter operation: ")

        if operation.lower() == "quit":
            print("Exiting calculator...")
            break

        if operation in ['+', '-', '*', '/']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2

            print("Result:", result)

        elif operation.lower() == "log":
            num = float(input("Enter number: "))
            base = float(input("Enter base: "))

            result = math.log(num, base)
            print("Result:", result)

        elif operation.lower() in ['sin', 'cos', 'tan']:
            angle_deg = float(input("Enter angle in degrees: "))
            angle_rad = math.radians(angle_deg)

            if operation.lower() == "sin":
                result = math.sin(angle_rad)
            elif operation.lower() == "cos":
                result = math.cos(angle_rad)
            elif operation.lower() == "tan":
                result = math.tan(angle_rad)

            print("Result:", result)

        elif operation.lower() in ['asin', 'acos', 'atan']:
            value = float(input("Enter value: "))

            if operation.lower() == "asin":
                result = math.degrees(math.asin(value))
            elif operation.lower() == "acos":
                result = math.degrees(math.acos(value))
            elif operation.lower() == "atan":
                result = math.degrees(math.atan(value))

            print("Result:", result)

        else:
            print("Invalid operation. Please try again.")


if __name__ == "__main__":
    calculator()
