### Exception handling Division by Zero
# num1 = int(input("please, Enter the first number: "))
# num2 = int(input("please, Enter the second number: "))
# try:
#     divide = num1/num2
#     print(divide)

# except Exception:
#     print("can not divide a number by zero!")

### FileNotFoundError
# try:
#    f = open('oop_concepts.py')
#    print("file opened")
# except FileNotFoundError as e:
#     print(e)

### ValueTooHighError

class ValueTooHighError(Exception):
    def __init__(self, value, message = "value is too high"):
        self.value = value
        self.mes = message
        super().__init__(self.message)

def check_value(number):
    """Function to check if the number is greater than 100 and raise ValueTooHighError."""
    if number > 100:
        raise ValueTooHighError(number)

#Test the custom exception
try:
    num = float(input("Enter a number: "))
    check_value(num)
    print("The number is within the acceptable range.")
except ValueTooHighError as e:
    print(f"ValueTooHighError: {e.message}. Value provided: {e.value}.")
except ValueError:
    print("Invalid input! Please enter a numeric value.")    
