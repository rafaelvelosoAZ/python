print("Welcome to the tip calculator")
bill = input("What was the total bill? \n" + "$")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? \n")
split = input("How many people to split the bill? \n")
cost = int(percentage) / 100
calc1 = (float(bill) * int(cost)) + float(bill)
calc2 = float(calc1) / int(split)
calc3 = float(round(calc2, 2))
print(f"Each person should pay: ${calc3}")
