amount = int(input("Enter your amount:   "))
if amount >= 50:
    amount += amount * (0.1)
else:
    amount += amount * (0.05)
print(amount)
