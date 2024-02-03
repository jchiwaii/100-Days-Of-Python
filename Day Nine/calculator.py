from ascii import logo
print(logo)

def calculator():
    while True:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                continue
        else:
            print("Error: Invalid operator.")
            continue

        print(f"The result is {result}")

        should_continue = input("Do you want to continue? Type 'yes' or 'no': ")
        if should_continue.lower() == 'no':
            break

calculator()