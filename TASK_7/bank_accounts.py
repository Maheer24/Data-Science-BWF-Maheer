class balanceException(Exception):
    pass

class bankAccount():
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.accountName = accountName

    def createAccount(self):
        print(f"\nAccount {self.accountName} created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.accountName}'.\nBalance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise balanceException(
                f"\nSorry account '{self.accountName}' only has a balance of ${self.balance:.2f}"
            )
        
    def withDraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except balanceException as error:
            print(f"\nWthdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print('\n************\n\nBeginnning Transfer.. 🌟')
            self.viableTransaction(amount)
            self.withDraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete!✅ \n\n**********")
        except balanceException as error:
            print(f"Transfer interrupted!. {error}")

class InterestRewardsAcct(bankAccount):

    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\n Deposit Complete.")
        self.getBalance()

class SavingsAccount(InterestRewardsAcct):

    def __init__(self, initialAmount, accountName):
        super().__init__(initialAmount, accountName)
        self.fee = 5

    def withDraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
            self.getBalance()
        except balanceException as error:
            print(f"\nWthdraw interrupted: {error}")
      