# 🛒 Shopping Cart Program

A simple Python shopping cart that lets you add items with prices and prints a full bill summary at the end.

## 📌 About

This project simulates a basic shopping cart where the user can keep adding food items and their prices. When done, it displays a neatly formatted bill with each item and the total amount.

## ⚙️ How it works

1. 🛍️ User types the name of a food item they want to buy
2. 💰 User enters the price of that item
3. 🔁 This repeats until the user types `Q` to quit
4. 🧾 A bill summary is printed showing all items and their prices
5. 💵 Total amount is displayed at the bottom

## 🖥️ Example
Type The Food You Want To Buy OR Type Q to Exit: pizza
Type The Price: 50
Type The Food You Want To Buy OR Type Q to Exit: burger
Type The Price: 120
Type The Food You Want To Buy OR Type Q to Exit: Q
----- Bill Summary -----
pizza : ₹50.00
burger : ₹120.00
Total Amount: ₹170.00

## 🧠 Concepts used

- `while True` loop with `break`
- `list.append()` for storing items and prices
- `zip()` to pair two lists together
- f-strings with `:.2f` for formatting prices
- `.lower()` for case-insensitive quit check