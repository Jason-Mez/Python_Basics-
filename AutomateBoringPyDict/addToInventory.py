dragonLoot = ["gold coin",
              "dagger",
              "gold coin",
              "gold coin",
              "ruby"
              ]

inv = {"gold coin": 42,
       "rope": 1
    }


def addToInventory(your_list: list, your_dict: dict):
    for i in dragonLoot:
        if i not in inv:
            inv[i] = dragonLoot.count(i)
        else:
            inv[i] += 1
    total_items = 0
    for y,z in inv.items():
        print(f"{y}: {z}")
        total_items += z
    print(f"The total amount of items are : {total_items}")


addToInventory(dragonLoot, inv)



