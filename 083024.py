#Exercise Inventory System for small store

#Creating inventory | Initializing tuple & dictionary 
store_fruits = ('banana', 'apple', 'orange', 'cherry', 'grape')
fruit_inventory = { #Keys = tuple items value = qty of fruits in stock 
    store_fruits[0] : 50,
    store_fruits[1] : 34,
    store_fruits[2] : 59,
    store_fruits[3] : int(40),
    store_fruits[4] : int(28)
}
#Update inventory 
#Reducing qty of orange by 12 because it's on sale 
fruit_inventory['orange']= 47
#New shipment arrived, so we must modify the qty of our grapes by 5
fruit_inventory['grape'] = 33
#Adding new fruit to tuple and dict| 
#Since tuples are unchangeable, we convert store_fruits into a list, use append method to add a new fruit, then convert it back into a tuple 
store_fruits_list = list(store_fruits)
store_fruits_list.append('kiwi')
store_fruits = tuple(store_fruits_list)
#Add last tuple item (our new fruit) to our dictionary and assigning it a qty of 10 
fruit_inventory[store_fruits[5]] = int(10)
#Analyze the inventory 
qty_check = 35
# for each fruit(key) item in our dict, if qty (value) is less than 35, print the fruit(key)name
for fruit, qty in fruit_inventory.items():
    if qty < qty_check:
        print('Items with a qty of less than 35 ->', fruit)
# Checks for 'mango' at each item in our dictionary, if it exists, print yes, else, print it doesn't exist
for name, check in fruit_inventory.items():
    if 'Mango' in name:
        print('Yes, mango does exist in our inventory')
    else:
        print('Mango doesn\'t exist in inventory')
#if 'Mango' not in fruit_inventory:
    #print("Mango doesn't exist in inventory")

#Remove and Display
fruit_inventory.pop('cherry')
print('Updated dictionary after removing cherry ->', fruit_inventory)