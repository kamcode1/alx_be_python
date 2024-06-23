income = input("Enter your monthly income:")
expenses = input("Enter your total monthly expenses:")

Monthly_Saving = int(income) - int(expenses)
Projected_Savings = Monthly_Saving * 12 + (Monthly_Saving * 12 * 0.05)
print("Yout monthly savings are ",  Monthly_Saving)
print("Projected savings after one year, with interest, is: ", Projected_Savings)