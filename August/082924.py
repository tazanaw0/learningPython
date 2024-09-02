#Exercise: Tuples and Dictionaries Together

#Initializing Tuple & Dictionary 
fruits = ('Banana', 'Blueberries', 'Orange', 'Cherries')
print(type(fruits))
fruit_prices = {
    fruits[0] : .60,
    fruits[1] : 3.99, 
    fruits[2] : 4.24, 
    fruits[3] : 3.89
}
print(type(fruit_prices))

#Access and Update
blue_price = fruit_prices.get('Blueberries')
print('The price of the second item in our tuple ->', blue_price)
#Or 
print('|| \nPrice of Blueberries ->',fruit_prices['Blueberries'])
fruit_prices.update({'Cherries': 3.45}) #since, we're changing value of dictionaries, it's important to use same syntax used to create items '{key:value}'
print('Updated price of \'Cherries\' now that they\'re on sale ->', fruit_prices[fruits[3]])

#adding new fruits w/o modify tuples(Would req conv tuple to list)
fruit_prices['Apples'] = 4.89
print('Updated fruit prices after inserting new fruit into dictionary ->', fruit_prices)