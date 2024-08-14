#Exercise: Shopping list manager
#Create a program that manages a shopping list

#Variables 

shopping_list = list(('Amiri', 'Tru Religion', 'United States Polo Assassin', 'Nike Tech', 'v2 YZY Boost', 'Nautica Tee', 'Doc Martin Boots'))

shopping_list_length = len(shopping_list)
print('The number of items in our list is:', shopping_list_length)
shopping_list_type = type(shopping_list)
print('Our list\'s data type is:', shopping_list_type)
#Print first, middle, and last list items 
print('Our first list item:', shopping_list[0])
print('Our middle item is:', shopping_list[len(shopping_list)// 2])

#Check if item exists in list 
specific_item = 'amiri'
print(f'Item {specific_item} exists in the list:', specific_item in shopping_list)
#Change item at 2nd index
shopping_list[2] = 'Polo Ralph Lauren'
print('Our updated list after changing the 2nd index:', shopping_list)
shopping_list[1:5] = 'Fubu Jeans', 'Denim Tears', 'Carhartt Jacket', 'UA Hoodie' 
print('Our updated list after changing items from the 1st to 4th index:', shopping_list)
print('Our updated list after inserting a new item at 3rd index:', shopping_list.insert(3, 'Nike Ski Mask'))
print('Our updated list after appending \'Tech Fleece\' to the end of our list', shopping_list.append('Tech Fleece'))

#New list created so we can add its values to our existing shopping_list
shopping_list1 = list(('Levi Denim Jeans', 'Hyper Denim Joggers', 'Adidas Sweats'))
print('Our updated shopping list after appending another list to our previous list.', shopping_list.extend(shopping_list1))
print('Our list after removing \'Adidas Sweats\':', shopping_list.remove('Adidas Sweats'))
print('Our list after popping the last item:', shopping_list.pop())
shopping_list.remove('Amiri')
print('Our list after deleting the item at the first index:', shopping_list)

#Clear the list and print results 
print('The results of us clearing our list:', shopping_list.clear())

Math = 2000 * 75 + (9-7 + 500%8)
Math1 = 2000 * 75 + (9-7 + 500%8) - 9000
Math2 = (2000 * 75) + (9-7 + 500%8) / 8
Math3 = (2000 * 75) + (9-7 + 500%8 / 8)

print(f'The results of our variable dubbed \'Math\' equation = {Math}')
print(f'The results of our variable \'Math1\' equation = {Math1}')
print('The results of our variable Math2 equation =', Math2)
print('The results of our variable Math3 equation =', Math3)