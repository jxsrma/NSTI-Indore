p1 = 50
p2 = 30
p3 = 60

prices = []

prices.append(p1)
prices.append(p2)
prices.append(p3)


prices[1] = 33
print(prices)
print("expensive: ",max(prices))
print("Cheapest: ",min(prices))