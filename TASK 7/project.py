from bank_accounts import *

Dave = bankAccount(1000,"Dave")
Sara = bankAccount(2000,"Sara")

Dave.getBalance()
Sara.createAccount()

Sara.deposit(4000)

Sara.withDraw(10)
Dave.transfer(100,Sara)

Jim = InterestRewardsAcct(1000,"Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100,Dave)

Blaze = SavingsAccount(1000,"Blaze")
Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(10000,Sara)