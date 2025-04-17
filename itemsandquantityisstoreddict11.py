inventory = {
    "Apples": 50,
    "Bananas": 30,
    "Oranges": 20,
    "Grapes": 40
}

print("Currnet Inventory: ")
for item, quantity in inventory.items():
    print(f"{item}: {quantity}")


item_to_sell = input("\nEnter the name of the item you want to sell: ").capitalize()
quantity_to_sell = int(input("Enter the quantity to sell: "))

if item_to_sell in inventory:
    if inventory[item_to_sell] >= quantity_to_sell:
        inventory[item_to_sell] -= quantity_to_sell
        print(f"\nsold {quantity_to_sell} {item_to_sell} (s). Remaining stock:{inventory[item_to_sell]}")
    else:
        print(f"\nNot enough stock to sell{quantity_to_sell} {item_to_sell}(s).Only{inventory[item_to_sell]}left.")


else:
    print(f"\nItem {item_to_sell} not found in the inventory.")

print("\nUpdated Inventory: ")
for item, quantity in inventory.items():
    print(f"{item}:{quantity}")
