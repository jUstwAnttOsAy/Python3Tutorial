import openhome.xmath as math

print(math.max(10, 5))
print(math.sum(1, 2, 3, 4, 5))
print(math.pi)

import openhome.bank as bank

acct = bank.Account('Justin', '123-4567', 1000)
acct.deposit(500)
acct.withdraw(200)
print(acct)