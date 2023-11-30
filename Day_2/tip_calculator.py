#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))

tip_percentage = int(input("What porcentage tip wpuld you like to give? 10, 12 or 15? "))
tip_percentage = tip_percentage / 100

total_people = int(input("How many people to split the bill? "))

bill_plus_tip = total_bill * (1 + tip_percentage)

total_each = round(bill_plus_tip / total_people, 2)

print(f"Each person should pay: ${total_each}")


