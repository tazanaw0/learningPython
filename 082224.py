#Exercise: Inventory Management w/ sets (GPT)
#Create a program that manages an inventory using sets

#Initializing Sets + printing set to confirm items were added
current_inventory = {'Deodorant', 'Shampoo', 'Conditioner', 'Shaver', 'Ice Roller'}
print('Set values ->', current_inventory)

#Checking if item exists in set
check_item = 'Shaver'
if check_item in current_inventory:
    print(f"Yes, '{check_item}' is in our set.")

print("conditioner" in current_inventory) #False

#Adding items to our set
current_inventory.add('Body Wash')
current_inventory.add('Face Wash')

#Creating new set #Dup added to demonstrate dups aren't allowed in sets
new_shipment = {'Cologne', 'Beard Oil', 'Face Wash'}

#Updating prev set w/ values from new set
current_inventory.update(new_shipment)
print("Updated inventory after including new_shipment ->", current_inventory)

#Removing items from set
current_inventory.remove('Cologne')
current_inventory.discard('beard oil') #No error occurred, discard() doesn't raise errors
#Removes random item from set
print(current_inventory.pop())

#Clearing set + printing the empty set 
new_shipment.clear()
print("Updated 'new_shipment' set after clearing it ->",new_shipment)

#Deleting set 
del new_shipment

#Additional Challenge 
#Loop through set and print items in alphabetical order (type conversion(list))

inventory_list = list(current_inventory)
inventory_list.sort()

for x in inventory_list:
     print(x)