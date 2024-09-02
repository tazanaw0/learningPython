#Exercise: Shopping List Management
#Program that manages a shopping list for different occasions

#Creating and Initializing Lists

groceries = ['Bread', 'Eggs', 'Tea', 'Spinach', 'Ground turkey', 'Tomatoe sauce', 'Tea', 'Pasta', 'Sliced turkey', 'Provolone cheese', 'Tea', 'Chips']
household_items = list(('Deodorant', 'Toothbrush', 'Toothpaste', 'Body wash', 'Shampoo', 'Conditioner', 'Face wash', 'Ice roller', 'Eye cream'))
#joining two lists together into a single list dubbed shopping_list
shopping_list = groceries + household_items
print(shopping_list)
#for item in household_items:
#   groceries.append(item)
#print(groceries)

#Checking to see how many times we've got the same value within our list 
# using count method
print("Number of 'Tea' items in our shopping list?", shopping_list.count('Tea'))

#intialized variable to practice using f strings + 
# we use the index method to return the first occurence's index of 'Ground turkey' item. 
lf_index = 'Ground turkey'
print(f"What index is our '{lf_index}' located at:", shopping_list.index('Ground turkey'))

#Practicing other List Operations 
#Adds (or extends) two values to our shopping list
shopping_list.extend(['Olive oil', 'Honey'])
print('Updated list after using extend to add 2 items:', shopping_list)

#Prints the item we chose to remove alongside removing it from our shopping_list
print('Item we will remove from list:', shopping_list.pop(-1))
print("Updated list after removing 'Honey' from our list:", shopping_list)

#Sorting our list in alphabetical order (asc)
shopping_list.sort()
print('Sorted shopping list:', shopping_list)

#Sortin our list in alphabetical order (desc)
shopping_list.sort(reverse = True)
print('Sorted shopping list in descending order:', shopping_list)

#Changes sort back to ascending order 
shopping_list.sort()

#Making a copy of 'shopping_list' and clearing it
Shopping_List = shopping_list.copy()
shopping_list.clear()

print("New var/list dubbed 'Shopping_List,' which is a copy of our original list 'shopping_list':", Shopping_List)

print("Result of using clear method to remove every item in 'shopping_list':", shopping_list)

