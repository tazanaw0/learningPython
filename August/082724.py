#Exercise: Dictionary Manipulation 
#Quick Exercise to reinforce dict skills

#Initializing dict 
#Key = book name value = qty
book_inventory = {
    "Charlie Bone": 8, 
    "Harry Potter" : 7, 
    "Percy Jackson & the Olympians" : 5
}

#Update and access 
book_inventory["Charlie Bone"] += 5 #Adding 5 more copies 
x = book_inventory.get('Harry Potter') #accessing harry potter values (qty of copies)
print("Number of 'Harry Potter' copies in stock ->", x)

#Remove and print
book_inventory.pop('Percy Jackson & the Olympians')
print("Updated book inventory post removal of 'Percy Jackson' -> ", book_inventory)