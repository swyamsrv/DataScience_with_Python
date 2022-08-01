amt = int(input("How Much kg of apples you want??  "))
if amt >= 5:
    price = 80
else:
    price = 90 
total = amt*price
print("You have to pay Rs. {} for {} Kg. of Apples.\n ".format(total, amt))