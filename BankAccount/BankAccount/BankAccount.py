class Account:

    def __init__(self, filepath):
        with open(filepath, 'r+') as file:
            self.balance = int(file.read())

    def getBalance(self):
        return self.balance

account = Account("balance.txt")
print(account.getBalance())
