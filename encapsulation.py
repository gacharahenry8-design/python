class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    def set_balance(self,balance):
        if balance > 0:
            self.__balance = balance
            return balance
        else:
            print("Invalid Data")
bank_account1 = BankAccount("Peter",2000)
print(str(bank_account1.name)+":"+str(bank_account1.set_balance(5000)))
# print(bank_account1.name)
# print(bank_account1.balance)
# bank_account1.balance = 5000
# print(bank_account1.balance)
# bank_account1.balance = -1000
# print(bank_account1.balance)