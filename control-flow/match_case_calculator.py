num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator = input("choose the operation(+, -, *, /): ")

match operator:
    case "+" : 
        operator = num1 + num2
        print(f"The result is {operator}")
    case "-" : 
        operator = num1 - num2
        print(f"The result is {operator}")
    case "*" : 
        operator = num1 * num2
        print(f"The result is {operator}")
    case "/" : 
        if num2 != 0:
            operator = num1/num2 
            print(f"The result is {operator}")   
        else:
            print("cannot divide by zero")
