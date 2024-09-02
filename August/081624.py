#Exercise: To-Do List Manager
#Create a program that manages a to-do list

To_Do = list (('Call Potomac Edison', 'Call Comcast', 'Uber Eats for funds', 'Organize stuff', 'Clean house', 'Get haircut',))

#Num_Of_Task = len(To_Do)
print('Total number of tasks:', len(To_Do))
print('List type:', type(To_Do))
print('Item at first index:', To_Do[0])
print('Item at middle index:', To_Do[len(To_Do)// 2])
print('Item at last index:', To_Do[-1])

Item_Check = 'Haircut'
print(f"Check and see if '{Item_Check}' is in our list:", Item_Check in To_Do)

To_Do[2] = 'Doordash for funds'
print('Updated List after changing our second index:', To_Do)
To_Do[-2:] = ['Schedule Haircut Appointment', 'Cardio']
print('Updated list after changing items using negative indexing:', To_Do)
To_Do.insert(6, 'In-Home Workout')
print('Updated list after inserting at 6th index:', To_Do)
To_Do.append('Target Pickup')
print('Updated list after appending an item to the end:', To_Do)
To_Do.extend(['Clean House', 'Update Dad'])
print('Updated list after extending the list w/ multiple items:', To_Do)
To_Do.remove(To_Do[3])
print('Updated list after removing the 3rd index:', To_Do)
Pop_Item = To_Do.pop()
print('Popped item from list:', Pop_Item)
print('Updated list after popping the last item:', To_Do)
del To_Do[4]
print('Updated list after using \'del\' to remove 4th index', To_Do)
To_Do.clear()
print('Updated list post clear method:', To_Do)

#Operator Precedence 
Equation = 9 * 8 - (50 % 11)
Equation1 = 2500/ 25 + (90 * 8)
Equation2 = (4000 % 28 * 10) + 85 // 10

EquationStr = '9 * 8 - (50 % 11)'
EquationStr1 = '2500/ 25 + (90 * 8)'
EquationStr2 = '(4000 % 28 * 10) + 85 // 10'

print(f'The results of {EquationStr} =', Equation)
print(f'The results of {EquationStr1} =', int(Equation1))
print(f'The results of {Equation2} =', Equation2)