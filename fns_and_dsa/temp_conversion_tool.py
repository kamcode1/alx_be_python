FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
        converted_value = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f"{fahrenheit}°F is {converted_value}°C")
def conver_to_fahrenheit(celsius):
        converted_value = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        print(f"{celsius}°C is {converted_value}°F")

def main():
    try:   
        to_be_converted = float(input("Enter the temperature to convert: "))
    except ValueError:
         print("Invalid temperature. Please enter a numeric value.")    
         return
    data_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if data_type == "F":
        convert_to_celsius(to_be_converted)

    elif data_type == "C":
        conver_to_fahrenheit(to_be_converted)

    else:
        print("Invalid Unit ")


if __name__ == "__main__":
    main()