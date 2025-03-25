menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []  # Stores (food, quantity) tuples
total = 0

# Display menu
print("-----------MENU-----------")
for key, value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("--------------------------")

# Order input loop
while True:
    # Ask for food item first
    food = input("Enter the name of the item (q to quit): ").lower()
    if food == "q":
        break  # Quit when user enters 'q'

    # Check if the food item exists in the menu
    if menu.get(food) is None:
        print("Item not found. Please enter a valid menu item.")
        continue  # Skip to the next loop iteration

    # Ask for quantity
    quantity_input = input(f"Enter the quantity of {food}: ")
    
    # Validate quantity input
    if not quantity_input.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    quantity = int(quantity_input)  # Convert to integer
    cart.append((food, quantity))  # Store food and quantity in cart

# Display order summary
print("-----------YOUR ORDER-----------")
for food, quantity in cart:
    price = menu.get(food) * quantity  # Calculate total price for this item
    total += price  # Add to grand total
    print(f"{quantity} {food} - ${price:.2f}")

print("--------------------------")
print(f"Your total is: ${total:.2f}")
