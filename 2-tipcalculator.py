print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill?\n"))

people = int(input("How many people will split the bill?\n"))

percentage = int(input("What percentage tip would you like to give? 10, 12 or 15\n"))

calculation = total_bill/people*(1+(percentage/100))
round_calculation = round(calculation, 2)

print(f"Each person should pay ${round_calculation}")