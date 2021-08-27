#Inventory

inventory = {
    "arrow": 12,
    "gold coin": 42,
    "Rope": 1,
    "torch": 6,
    "dagger": 1,
}

def displayInventory(dictionary: dict):
    total_items = 0
    for i in inventory.values():
        total_items += i
    return f"The total number of items are {total_items}"

total_number = displayInventory(inventory)
print(total_number)