number_item = int(input("Number of items:"))
total = 0

for i in range(number_item):
    price_item = float(input("Price of item:"))
    total += price_item

print("Total price for", number_item, "items is $", total)
