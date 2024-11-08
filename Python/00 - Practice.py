
list_of_items ={
    1 : "biscuits",
    2 : "cereals",
    3 : "chicken",
    4 : "oats",
    5 : "rice"
}

item_quantity_in_store = {
    "biscuits": 5,
    "cereals": 4,
    "chicken": 6,
    "oats": 7,
    "rice": 20
}


# Define item costs
item_costs = {
    "biscuits": 20.50,
    "cereals": 90.00,
    "chicken": 200.00,
    "oats": 39.99,
    "rice": 79.99
}


while True:
    print("\n--- Items Available ---")
    print(f"{'Item':<15}{'Quantity':<15}{'Item / Cost':<10}")
    print("-" * 50)
    for item_id in list_of_items.values():
        item_name = item_id
        print(f"{item_name:<15}{item_quantity_in_store[item_name]:<15}{item_costs[item_name]}")

    # Input quantities
    biscuits_quantity = int(input("How many biscuit packets are required? "))
    cereals_quantity = int(input("How many cereal packets are required? "))
    chicken_quantity = int(input("How many frozen chicken packets are required? "))
    oats_quantity = int(input("How many oats packets are required? "))
    rice_quantity = int(input("How many rice packets are required? "))

    # Validate quantities and add to cart
    for item_name, quantity in zip(list_of_items.values(), [biscuits_quantity, cereals_quantity, chicken_quantity, oats_quantity, rice_quantity]):
        if quantity <= item_quantity_in_store[item_name]:
            print(f'{quantity} {item_name} added to cart !!')
        else:
            print(f'{quantity} {item_name} are not available in store, available are {item_quantity_in_store[item_name]}')
            quantity = int(input(f"Please select as per available stock! Your quantity is: "))
            while quantity > item_quantity_in_store[item_name] or quantity < 0:
                if quantity > item_quantity_in_store[item_name]:
                    print("Please select only available quantity")
                quantity = int(input(f"Please select as per available stock! Your quantity is: "))
            print(f'{quantity} {item_name} added to cart !!')

    # Calculate total cost
    total_cost = (
        biscuits_quantity * item_costs["biscuits"] +
        cereals_quantity * item_costs["cereals"] +
        chicken_quantity * item_costs["chicken"] +
        oats_quantity * item_costs["oats"] +
        rice_quantity * item_costs["rice"]
    )

    # Input delivery details
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    delivery_distance = int(input("Distance from store (5/10/15 km): "))

    delivery_charge = 0
    if delivery_distance > 15:
        delivery_charge += 30

    Bill = (total_cost + delivery_charge)

    # Print the bill
    print("\n--- Bill ---")
    print(f"{'Item':<15}{'Quantity':<15}{'Total-Cost'}")
    print("-" * 50)
    for item_name, quantity in zip(list_of_items.values(), [biscuits_quantity, cereals_quantity, chicken_quantity, oats_quantity, rice_quantity]):
        if quantity > 0:
            print(f"{item_name:<15}{quantity:<15}{quantity * item_costs[item_name]}")

    print(f'\nTotal cost : ₹ {total_cost}')
    print(f"\nTotal Cost: ₹{total_cost} + ₹{delivery_charge} = ₹{Bill} Rs/- \n")
    print(f"Delivery Details:\nName: {name}\nAddress: {address}")

    # Update item quantities in store
    item_quantity_in_store["biscuits"] -= biscuits_quantity
    item_quantity_in_store["cereals"] -= cereals_quantity
    item_quantity_in_store["chicken"] -= chicken_quantity
    item_quantity_in_store["oats"] -= oats_quantity
    item_quantity_in_store["rice"] -= rice_quantity

    print("\n--- Updated Stock ---")
    print(f"{'Item':<15}{'Updated Quantity'}")
    print("-" * 30)
    for item_name in list_of_items.values():
        print(f"{item_name:<15}{item_quantity_in_store[item_name]}")

    add_items = input("Do you want to continue shopping? (y/n): ").strip().lower()
    if add_items != 'y':
        print(f'Mr/Miss {name}, have a good day!')
        break

