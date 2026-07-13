# Compound Interest Calculator

principal = float(input("enter the principal amount: "))
rate = float(input("enter the rate of interest: "))
time = int(input("enter the time of interest: "))


while principal <= 0:
    print("principal amount cannot be zero")
    principal = float(input("enter the principal amount: "))


while rate <= 0:
    print("rate of interest cannot be zero")
    rate = float(input("enter the rate of interest: "))


while time <= 0:
    print("time of interest cannot be zero")
    time = int(input("enter the time of interest: "))


amount = principal * (1 + rate / 100) ** time

compound_interest = amount - principal

print(f"compound interest is: ₹{compound_interest}")