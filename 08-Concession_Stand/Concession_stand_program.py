concession = {
    "popcorn": 1.00,
    "hotdog": 2.00,
    "giant pretzel": 2.00,
    "asst candy": 1.00,
    "soda": 1.00,
    "bottled water": 1.00
}

for key, value in concession.items():
    print(f"{key}: {value}")

again = "y"
total = 0

while again == "y":
    order = input("Enter The Items You Want To Order: ").lower()
    total = total + concession[order]
    again = input("Add Another Item: (Y For Yes / N For No): ").lower()

print(f"Your total is: ${total}")