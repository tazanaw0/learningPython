#Exercise: Working w/ Tuples (GPT)
#Create a program that manages a collection of items using tuples

#Initalize tuple w/ 5 items
fruits = ('Apple', 'Banana', 'Orange', 'Blueberry', 'Kiwi')

#Accessing items in tuple 
#Prints 2nd and 4th item in our tuple
print(f'2nd item in tuple: {fruits[1]} \n4th item in tuple: {fruits[3]}')

#Updating tuples
#Modifying tuple by converting it to a list, inserting an item at the end and converting it back to a tuple. 
h = list(fruits)
h.insert(5, 'Watermelon')
fruits = tuple(h)
print('Update tuple after inserting item at 5th index:', fruits)

(a, b, c, *rest) = fruits
print('Unpacking the first three items from our tuple:', a +"|" + b + "|" + c)
print('Remaining items unpacked from fruit tuple:', rest)


#Loop to print each item in our fruits tuple + the corresponding index
a = 0 
while a < (len(fruits)):
    print(f'{a}: {fruits[a]}')
    a = a + 1
#Initializing another tuple dubbed vegetables w/ 3 items
vegetables = tuple(('Tomatoe', 'Spinach', 'Corn'))

#Joining fruit and vegetable tuples together into food_items tuple
food_items = fruits + vegetables
print('Result of joining our fruits and vegetables tuple:', food_items)

#Modifying our tuple by converting into a list, so we can have > 1 occurence of the same fruit in our list
L = list(food_items)
L.append('Watermelon')
food_items = tuple(L)
print(food_items)

#Counts # of times item occurs in our tuple
print('# of times watermelon occurs in our tuple:', food_items.count('Watermelon'))

#Prints index position where the first occurence of the item is in our tuple
print("Index position of 'Spinach' in our tuple:", food_items.index('Spinach'))
