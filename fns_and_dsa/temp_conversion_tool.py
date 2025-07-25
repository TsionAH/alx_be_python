FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
data = input("Enter temperature: ")
type_of_data = input("Is this temperature in Fahrenheit or Celsius? (F/C): ").strip().upper()
if type_of_data == 'F':
    converted_temp = convert_to_celsius(float(data))
    print(f"{data}°F is {converted_temp}°C")
elif type_of_data == 'C':
    converted_temp = convert_to_fahrenheit(float(data))
    print(f"{data}°C is {converted_temp}°F")
else:
    print("Invalid input. Please enter 'F' for Fahrenheit or 'C' for Celsius.")