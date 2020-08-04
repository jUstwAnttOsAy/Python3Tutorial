#Class用於將狀態與功能結合
#未使用Class, 相關功能與物件分開
import bank
acct = bank.account('Justin', '123-4567', 1000)
bank.deposit(acct, 500)
bank.withdraw(acct, 200)
print(bank.to_str(acct))

#使用Class, 把需要用的函示寫入組織再一起
class Account:
    # 建構式
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
             raise ValueError('amount must be positive')
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise RuntimeError('balance not enough')
        self.balance -= amount

    #字串化
    def __str__(self):
        return 'Account({0}, {1}, {2})'.format(
            self.name, self.number, self.balance)

acct = Account('Steve', '012-345-678', 1000)
acct.deposit(200)
acct.withdraw(500)
print(acct)

#套件
#import pack.modu =>尋找pack資料夾底下, 有無__init__.py, 有的話在該目錄底下尋找
#盡量讓__init__.py保持空白