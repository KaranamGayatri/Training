#Create a bank account class that has two attributes: owner, balance and 
#two methods: deposit, withdraw
#As an added requirement, withdrawals may not exceed the available balance.
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f'Account owner:  {self.owner}\nAccount balance: ${self.balance}'
    
    def deposit(self, dep_amt):
        self.balance += dep_amt
        print("Deposite Accepted")
    
    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")
# 1. Instantiate the class
acct1 = Account("Jose", 100)

# 2. Print the object
print(acct1)           # Account owner:   Jose
                       # Account balance: $100

# 3. Show the account owner attribute
print(acct1.owner)     # Jose

# 4. Show the account balance attribute
print(acct1.balance)   # 100

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)      # Deposit Accepted
acct1.withdraw(75)     # Withdrawal Accepted

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)    # Funds Unavailable!