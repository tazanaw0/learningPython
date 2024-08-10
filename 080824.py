#Exercise: Simple Inventory System
#Create a program that simulates a basic inventory system with the following tasks:

#Variables and Data Types
item_names = str('iPhone')
item_quantities = int(51)
item_prices = float(899.99)

itemnames1 = str('iPhone Charger')
item_quantities1 = int(51)
item_prices1 = float(24.99)

#Arithmetic Operations
total_inventory_price = item_quantities * item_prices
estimated_value= f"The total value of our inventory is estimated to be ${total_inventory_price}"
print(estimated_value)

#String Operations
inventory_description = str('For sale, we\'ve got brand new, factory sealed iPhone x\'s.')
inv_desc_length = len(inventory_description)
print (inv_desc_length)
inv_desc_lowercase = inventory_description.lower()
print(inv_desc_lowercase)
keyword_check = 'Sale' in inventory_description
print(bool(keyword_check)) #False

#Boolean Operations
in_stock = True
on_sale = False
is_new = True 

#Logical operators 
print('In stock and on sale:', in_stock and on_sale)
print('In stock or on sale:', in_stock or on_sale)
print('Not on sale:', not on_sale)
print('In stock and is new:', in_stock and is_new)

#Casting
print('You\'re expected to pay around',int(item_prices))
print('The number of iphone\'s we have in stock are', float(item_quantities))
quantity1_as_string = str(item_quantities1)
concatenated_string = 'We have ' + quantity1_as_string + ' iPhone chargers in stock.'
print('Concatenated String:', concatenated_string)



