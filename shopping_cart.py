foods = []
prices = []
total = 0
quantity = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of the food: $"))
        quantity = int(input("Enter the quantity: "))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")
for food in foods:
    print(food, end=" ")

for price in prices:
    total = price * quantity

print()
print(f"Your total is ${total:,.2f}")