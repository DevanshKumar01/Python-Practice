# 💰 Compound Interest Calculator

A simple Python program that calculates compound interest based on principal amount, rate of interest, and time period.

## 📌 About

This project takes user input and calculates how much interest will accumulate on an investment over time using the compound interest formula. It also includes input validation to make sure the user doesn't enter invalid values.

## ⚙️ How it works

1. 📥 Takes principal amount, rate of interest, and time period as input from the user
2. ✅ Validates that all values are greater than zero (keeps asking until valid input is given)
3. 🧮 Calculates the compound interest using the formula: Amount = Principal x (1 + Rate/100) ^ Time, then Compound Interest = Amount - Principal
4. 📊 Displays the compound interest, rounded to 2 decimal places

## 🖥️ Example

Enter the principal amount: 1000
Enter the rate of interest: 10
Enter the time period (in years): 1
Compound interest is: ₹100.0

## 🧠 Concepts used

- 🔢 Input handling with type conversion (float, int)
- 🔁 while loops for input validation
- ➕ Basic arithmetic operations
- 🎯 f-strings for formatted output

## 🚀 Run it

python compound_interest_calculator.py

## 📁 Part of

This project is part of my Python Practice repository: https://github.com/DevanshKumar01/Python-Practice
