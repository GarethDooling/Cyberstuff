class Budget():
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name 

    def __repr__(self):
        return f"The remaining budget is {self.balance}."

    def withdraw(self, amount):
        self.balance -= amount 
        return amount 

    def deposit(self, amount):
        self.balance += amount
        return amount 