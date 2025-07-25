import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date.strftime("Current date and time: %Y-%m-%d %H:%M:%S"))
    
def calculate_future_date():
    future_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.datetime.now() + datetime.timedelta(days=future_days)
    print(future_date.strftime("Future date: %Y-%m-%d %H:%M:%S"))
display_current_datetime()
calculate_future_date()