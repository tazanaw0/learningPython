#Exercise: Library Book Manager
#Create a program that manages a list of books

Books = list(('Midnight for Charlie Bone', 
              'Charlie Bone and the Time Twister', 
              'Harry Potter and The Chamber of Secrets', 
              'Harry Potter and The Sorceror\'s Stone'))

print('Total number of books in our list:', len(Books))
print('Type of variable:', type(Books))
print('Book at the beginning of our List:', Books[0])
print('Book at the middle of our List', Books[len(Books) // 2]) 
print('Book at the end of our List', Books[-1])
checkFor = 'Harry Potter'
print(f'The following book \'{checkFor}\' exists in our list:', checkFor in Books)

Books[2] = 'Harry Potter and The Deathly Hallows'
print('Our list after changing the 2nd position:', Books)
Books[-2:] = ['The way of a superior man', 
                '48 Laws of Power']
print('Our updated list:', Books)
Books.insert(3, 'Rich Dad, Poor Dad')
print('Our updated after inserting:', Books)
Books.append('The Laws of Human Nature')
print(f'Updated list after appending a new one to the end', Books)
Books.extend(['Diary of a wimpy kid', 'Diary of a wimpy kid 2'])
print('Updated list after extending w/ two books:', Books)
Books.remove('Diary of a wimpy kid')
print('Updated list after removing \'Diary of a wimpy kid\':', Books)
bookPop = Books.pop()
print('Popped from list:', bookPop)
print('Updated list:', Books)
del Books[0]
print('Updated list after deleting first item:', Books)

Books.clear()
print('Updated list after clearing items:', Books)

#Operator Precedence 
Math = (45000 % 24 + 128000) - 12000 / 90 + (40000/ 8)
Math1 = 45 * 5 * (50 % 9) + 12000 / 80 #1275
Math2 = 45 / 5 * (50 // 8) # 54

print('Reults of(45000 % 24 + 128000) - 12000 / 90 + (40000/ 8):', int(Math))
print('Results of  45 * 5 * (50 % 9) + 12000 / 80:', Math1)
print('Results of 45 / 5 * (50 // 8):', Math2)