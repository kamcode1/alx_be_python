monthly_income = input("Enter your monthly income:")
monthly_expenses = input("Enter your total monthly expenses:")

monthly_Saving = int(monthly_income) - int(monthly_expenses)
Projected_Savings = monthly_Saving * 12 + (monthly_Saving * 12 * 0.05)
print("Yout monthly savings are ",  monthly_Saving)
print("Projected savings after one year, with interest, is: ", Projected_Savings)