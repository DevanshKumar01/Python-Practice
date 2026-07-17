foods = []
prices = []
total = 0

while True:
    food = input("Type The Food You Want To Buy OR Type Q to Exit: ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Type The Price: "))
        foods.append(food)
        prices.append(price)
        total += price

print("\n----- Bill Summary -----")
for f, p in zip(foods, prices):
    print(f"{f} : ₹{p:.2f}")

print("-------------------------")
print(f"Total Amount: ₹{total:.2f}")