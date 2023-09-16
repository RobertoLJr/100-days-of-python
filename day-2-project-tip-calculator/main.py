print("Welcome to the tip calculator.\n")

bill = float(input("What was the total bill? $ "))
people_count = int(input("How many people will split the bill? "))
tip_percentage = int(input("What tip percentage would you like to give (10, 12, 15)? "))

tip = bill * tip_percentage / 100
total_bill = bill + tip
bill_per_person = "{:.2f}".format(round(total_bill / people_count, 2))

print(f"Each person should pay $ {bill_per_person}")
