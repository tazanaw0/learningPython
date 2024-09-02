#Exercise: Tuple and List Manipulation 
#Converting the two, performing operations, and utilizing methods


#Creating and initializing data 
cities = ('D.C.', 'Ft. Washington', 'Alexandria', 'Oxon Hill', 'Waldorf')
countries = ['Ethiopia', 'Kenya', 'Sudan', 'Egypt', 'Morocco']

#Converting and manipulating 
city_list = list(cities)
city_list.extend(['Fairfax', 'Mclean'])
cities = tuple(city_list)
print('Updated tuple after adding two items and conversion ->', cities)

#Joining cities tuple with countries list 
cities = list(cities)
locations = cities + countries
print() #For readability in terminal 
print('Result of combined lists:', locations)

print('\'Kenya\'s\' position in our list:',locations.index('Kenya'))

#Initialize list w/ vowels 
vowels = list(('A', 'E', 'I', 'O', 'U'))

#Checks if first character in each item of our locations list begins w/ a vowel
for a in locations:
    if a[0] in vowels:
        print(a)

#Sorting our locations list alphabetically and printing it
locations.sort()
print(locations)

copy_locations = locations.copy()
print('Copied list ->', copy_locations)
locations.clear()
print('Updated locations list post clear ->', locations)
