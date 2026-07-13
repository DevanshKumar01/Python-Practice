# Temperature Converter
# Converts Celsius to Fahrenheit and Fahrenheit to Celsius


temperature = float(input("enter the temperature: "))
unit = input("Enter the unit (C/F): ").strip().upper()
if unit == "C":
    result = temperature * 1.8 + 32
    print(f"{round(result, 2)} °F")
elif unit == "F":
    result = (temperature - 32) / 1.8
    print(f"{round(result, 2)} °C")
else:
    print("Invalid unit! Please enter C or F.")