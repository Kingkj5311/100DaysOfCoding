# Tip Calculator
# Completed
print("Welcome to the tip calculator!.")
bill=input("What was the total bill? $")
percentage=input("What percentage tip would you like to give? 10, 12, or 15? ")
bill=float(bill)
percentage=int(percentage)
tip=bill*(percentage/100)
people=input("How many people to split the bill?")
people=int(people)
total_bill=bill+tip
bill_per_person=total_bill/people
print("Each person Should pay $%.2f " %bill_per_person)
# print(f"Each person Should pay ${bill_per_person}")
# print(f"Each person should pay ${bill_per_person:.2f}")