class BankAccount:
    _next_account_number = 1000
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder=account_holder
        self.balance=initial_balance
        self.account_number=BankAccount._next_account_number
        BankAccount._next_account_number += 1
        
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Deposit amount must be positive.")
        self.balance+=amount
        
    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("Withdraw Money should be positive")
        if amount>self.balance:
            raise ValueError("Insufficient Funds")
        self.balance-=amount
        
    def transfer(self,other_account_holder,amount):
        if not isinstance(other_account_holder,BankAccount):
            raise TypeError("Account Doesnt exists")
        self.withdraw(amount)
        other_account_holder.deposit(amount)
