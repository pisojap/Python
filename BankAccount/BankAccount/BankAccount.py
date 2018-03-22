class Account:
    """
    Account class is responsible for manage users account file
    """

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self): 
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    type = "checking"
    def __init__(self, filepath):
        Account.__init__(self, filepath)

    def transfer(self, amount, fee):
        self.fee = fee
        self.balance = self.balance - amount - fee

print(Checking.type)
checking = Checking("balance.txt")
checking.deposit(10)
checking.transfer(0, 1)
checking.commit()
print(str(checking.getBalance()))
print(Account.__doc__)