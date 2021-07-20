# numberSwords = 10
# NumberAxes = 15
# number_weapons = numberSwords + NumberAxes 
# print(number_weapons)

inventory = {"sword": {"value": 50, "quantity": 30},
              "sheild":{"value": 20, "quantity": 6},
              "helmet":{"value": 10, "quantity": 1}}

items = ["sword", "sheild", "helmet"]
c = ""

def menu():
  print("WELCOME TO INVENTORY")
  print("---------------------------------------")
  print("A - to add an item")
  print("R - to remove an item")
  print("E - to edit details of an item")
  print("L - to list all the items")
  print("D - to list details of all items")
  print("Q - to quit")
  
while( c != "Q" or c != "q"):
  menu() 
  c = input("What would you like to do? ")
  print()
  if c == "q" or c == "Q":
    break
  elif c == "a" or c == "A": #add item
    item_name = input("Enter item name: ").lower()
    
    exist = False
    for key, value in inventory.items():
      if (item_name in items):  
        exist = True 
    
    if (exist):
      print()
      print("This item already exists!")
    else:
      items_value = float(input("Enter item value: "))
      items_quantity = float(input("Enter itme Quantity: "))
      inventory[item_name] = {}
      inventory[item_name]["value"] = items_value 
      #add item to list
      items.append(item_name)
      print()
      print("Item added successfully")
  elif c == "r" or c == "R": #remove items
    print()
    name = input("Enter a item you want to remove ")

    if(name in items):
      del inventory[name]
      items.remove(name)

      print("Item successfully removed")
    else:
      print("this item doesnt exist!\n")
  
  elif c == "e" or c == "E":
    print()
    name = input("enter a item you want to edit ")
    if(name in items):
      item_name = input("Enter items new name: ")
      item_value = float(input("Enter items new value: "))
      item_quantity = int(input("Enter new quantity: "))

      del inventory[name]
      items.remove(name)
      inventory[item_name] = {}
      inventory[item_name]["value"] = item_value 
      inventory[item_name]["quantity"] = item_quantity 

      #add item to tracking list 
      items.append(item_name)
      print("success! Item edited")
    else:
      print("That item doesn't exist")

  elif c == "l" or c == "L":
    print("\nItems in inventory")
    
    for i in items:
      print(i)
    print()

  elif c == "d" or c == "D":
    print("\nDetails of all items in inventory: \n")
    
    for key, value in inventory.items():
      print("Item:", key)
      for key in value:
        print(key + ':', value[key])
      print()

  else:
    print()
    print("Not a valid option")