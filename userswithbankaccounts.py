class User:
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = account

    # def userTransfer(self, account, transferee):
    #     self.account -= amount
    #     print(self.name)
    #     print(self.account)
    #     transferee.account += amount
    #     print(transferee.name)
    #     print(transferee.account)


class BankAccount:
    def __init__(self, intrate=0.02, balanceChecking=10, balanceSaving=0):
        self.intrate = intrate
        self.balanceChecking = balanceChecking
        self.balanceSaving = balanceSaving

    def deposit(self, amount):
        self.balanceChecking += amount
        return self

    def withdraw(self, amount):
        self.balanceChecking -= amount
        return self

    def displayAccountInfo(self):
        print(self.intrate, self.balanceChecking)
        return self

    def yeildInt(self):
        self.balanceChecking += (self.balanceChecking*self.intrate)
        return self

    def accountTransfer(self, amount, accountType):
        self.balanceChecking -= amount
        accountType.balanceSaving += amount
        print("New Checking Balance" + balanceChecking,
              "New Saving Balance" + balanceSaving)
        return self


user1 = User('Matthew', 'matthew@gmail.com', BankAccount())
user2 = User('Mark', 'mark@gmail.com', BankAccount())
user3 = User('Luke', 'luke@gmail.com', BankAccount())


user1.account.deposit(100).deposit(50).deposit(
    25).withdraw(75).displayAccountInfo()


user2.account.deposit(200).deposit(300).withdraw(
    100).withdraw(1000).displayAccountInfo()


user3.account.deposit(1000).withdraw(100).withdraw(
    200).withdraw(300).displayAccountInfo()


# user1.account.accountTransfer(100, balanceSaving)
