class BankAccount:
    def __init__(self, account_balance = 0.00):
        self.account_balance = float(account_balance)
   
    def deposit(self, amount):
        self.account_balance += float(amount)
        return self.account_balance
    
    def withdraw(self, amount):
        if self.account_balance >= float(amount):
            self.account_balance -= float(amount)
            return True
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

            