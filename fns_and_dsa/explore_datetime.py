from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formated_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{formated_current_date}")

display_current_datetime()
def calculate_future_date():
    num_of_days = int(input("please, Enter the number of days: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(num_of_days)
    formated_future_date = future_date.strftime("%y-%m-%d")
    print(f"{formated_future_date}")
calculate_future_date()