# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# operator = input("choose the operation(+, -, *, /): ")

# match operator:
#     case "+" :
#         print(f"The result is {num1 + num2}")
#     case "-" : 
#         print(f"The result is {num1 - num2}")
#     case "*" : 
#         print(f"The result is {num1 * num2}")
#     case "/" : 
#         if num2 != 0: 
#             print(f"The result is {num1 / num2}")   
#         else:
#             print("cannot divide by zero")
#     case _:
#         print("Invalid operation. Please choose one of +, -, *, /.")
# match_case_calculator.py

# Prompt for User Input
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# operator = input("Choose the operation (+, -, *, /): ")

# Perform the Calculation Using Match Case
# match operator:
#     case "+":
#         result = num1 + num2
#         print(f"The result is {result}")
#     case "-":
#         result = num1 - num2
#         print(f"The result is {result}")
#     case "*":
#         result = num1 * num2
#         print(f"The result is {result}")
#     case "/":
#         if num2 != 0:
#             result = num1 / num2
#             print(f"The result is {result}")
#         else:
#             print("Cannot divide by zero.")
#     case _:
#         print("Invalid operation. Please choose one of +, -, *, /.")

# match_case_calculator.py

# Prompt for User Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

# Perform the Calculation Using Match Case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation. Please choose one of +, -, *, /.")