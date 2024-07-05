inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)

#Select the first element in inventory.
first = inventory[0]

#Select the last element from inventory. 
last = inventory[-1]

#Select items from the inventory starting at index 2 and up to, but not including, index 6.
inventory_2_6 = inventory[2:6]

#Select the first 3 items of inventory.
first_3 = inventory[:3]

#How many 'twin bed's are in inventory? 
twin_beds = inventory.count("twin bed")

#Remove the 5th element in the inventory. Save the value to a variable called removed_item.
removed_item = inventory.pop(4)

#There was a new item added to our inventory called "19th Century Bed Frame".
inventory.insert(10, "19th Century Bed Frame")

inventory.sort()
print(inventory)
