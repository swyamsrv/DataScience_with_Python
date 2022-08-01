product = input("What item did you buy?")
price = float(input("How much did you pay ?"))
quantity = int(input('Enter number of item??'))

print("You Purchased", quantity, product, 'for', price)

price = price - 0.25*price

print("The Final Price = {}".format(price))
