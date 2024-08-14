#Exercise: Movie Collection Manager
#Create a program that manages a list of movies:

#Variables + Lists
Movie_Collection = ['Madagascar', 'Cars', 'Cars 2 ', 'City of God', 'Harry Potter: Chamber of Secrets', 'Harry Potter: Deathly Hallows Pt. 1', 'Harry Potter: Deathly Hallows Pt.2', 'Kill Bill Vol. 1', 'Shrek', 'Shrek 2', 'Shrek the Third']
movie_length = len(Movie_Collection)
print(f'We have {movie_length} movies in our list')
movie_type = type(Movie_Collection)
print(f'The data type of our variable \'Movie_Collection\': {movie_type}')
print('The movie at our first index:', Movie_Collection[0])
Middle_Movie = Movie_Collection[len(Movie_Collection)// 2] # Divides total number of movies by 2 to get middle index
print(f'The movie at our middle index: {Middle_Movie}')
print('The movie at our last index:', Movie_Collection[-1])
Specific_Movie = 'Fast and Furious'
print(f'The following movie  \'{Specific_Movie}\' is in our list:', Specific_Movie in Movie_Collection)

Movie_Collection[2] = 'Cars 3'
print('Our updated list after replacing index 2 or \'Cars\':', Movie_Collection)
New_Movies = 'Transformers 1', 'Transformers 2', 'Transformers 3'
Movie_Collection[-1:-4] = 'Transformers 1', 'Transformers 2', 'Transformers 3'
print(f'Our updated list after changing the last 3 movie items w/ {New_Movies}:', Movie_Collection)
Movie_Collection.insert(3, 'Harry Potter and the Sorcerors\' Stone')
print('Updated movie list:', Movie_Collection)
Movie_Collection.append('Transformers 4')
print('Updated movie list:', Movie_Collection)
Movie_Collection.extend(['Transformers 5, Transformers 6'])
print('Updated list after extending our list w/ multiple movies:', Movie_Collection)
Movie_Collection.remove('Madagascar')
print('Updated list after removing our first index', Movie_Collection)
Last_Movie = Movie_Collection.pop()
print(f'Popped movie: {Last_Movie}')
print('Updated list after popping the last two index:', Movie_Collection)
del Movie_Collection[0]
print('Updated list after deleting the first movie in our list', Movie_Collection)
Cleared_List = Movie_Collection.clear()
print(f'After clearing our populated list, we\'re left with: {Cleared_List}')

Math = 2500 * 9 + (80%9 * 50)
Math1 = 80%9 * 50 - (40//8 +25)
Math2 = (1000 // 23 * 80 + 400) - 4000

print('2500 * 9 + (80%9 * 50) =', Math)
print('80%9 * 50 - (40//8 +25) =', Math1)
print('(1000 // 23 * 80 + 400) - 4000) =', Math2)
