# Weight Converter
# Converts kilograms to pounds and pounds to kilograms

weight = float(input("Enter your weight: "))
unit = input("Enter the unit (Kg/Lb): ").strip().lower()

if unit == "kg":
    result = weight * 2.205
    print(f"{weight} kg = {round(result, 2)} lb")

elif unit == "lb":
    result = weight / 2.205
    print(f"{weight} lb = {round(result, 2)} kg")

else:
    print("Invalid unit! Please enter either 'Kg' or 'Lb'.")