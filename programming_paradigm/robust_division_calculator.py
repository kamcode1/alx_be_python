def safe_divide(numerator, denominator):
    try:
        result = float(numerator)/float(denominator)
        print(f"The result of the division is {result}")
    except Exception:   
        print("Error: Cannot divide by zero.") 
    
    try:
        result = float(numerator)/float(denominator)
        print(f"The result of the division is {result}")
    except ValueError:
        print("Error: Please enter numeric values only.")