# Compound Interest Calculator

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time period (in years): "))


while principal <= 0:
    print("Principal amount cannot be zero or negative")
    principal = float(input("Enter the principal amount: "))

while rate <= 0:
    print("Rate of interest cannot be zero or negative")
    rate = float(input("Enter the rate of interest: "))

while time <= 0:
    print("Time period cannot be zero or negative")
    time = int(input("Enter the time period (in years): "))


# Calculate compound interest
amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

# Round to 2 decimal places for clean output
compound_interest = round(compound_interest, 2)

print(f"Compound interest is: ₹{compound_interest}")