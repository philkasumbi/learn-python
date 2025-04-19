
#write a python program to print the total of a shopping cart list
cart = [10,20,30,"five",70,100]
total = 0

for item_price in cart:
    if isinstance(item_price, str):
        continue
    total += item_price
print(f"The total cost is: {total}")


