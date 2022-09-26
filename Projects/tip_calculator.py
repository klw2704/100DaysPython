print("Welcome to the tip calculator.")
initial_bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_splitting = int(input("How many people split the bill? ")) 

split_price = ((((100 + tip_percentage)/100) * initial_bill) / people_splitting)

cost = "{:.2f}".format(split_price)

final_amount = f"Each person should pay £{cost}"

print(final_amount)