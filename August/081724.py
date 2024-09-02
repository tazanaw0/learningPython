#Exercise: Task Management System (GPT)
#Create a program that manages a task list

#Defining Lists
Tasks = list(('Upload to git', 'Read CB', 'Uber Eats', 'Clean house', 'Modify necessity list'))

Num_of_Task = len(Tasks)
print('Total number of tasks:', Num_of_Task)
print('Type of list:', type(Tasks))
print('Task at first index:', Tasks[0])
print('Tasks at middle index:', Tasks[len(Tasks)//2])
print('Task at last index:', Tasks[-1])
Check_for_task = 'Read CB'
if Check_for_task in Tasks:
    print(f'Yes, {Check_for_task} is present in our task list.')
## Or 
##print('Reading is present in our task list:', 'Read CB' in Tasks)
Tasks[2] = 'Doordash shift'
print('Updated list after changing 2nd index:', Tasks)
Tasks[-2:] = 'Organize house', 'Update Necessity List'
print('Updated list after changing items using negative indexing:', Tasks)
Tasks.insert(0, 'Update obsidian notes to reflect what I\'ve learned today')
print('Updated list after inserting a task at index 0:', Tasks)
Tasks.append('Cook protein and veggies for the week')
print('Updated list after appedning to end:', Tasks)
Tasks.extend(['Touch grass', 'Finish a track in Ableton']) #Dont forget brackets when using extend!
print("Updated list after extending it with two new items", Tasks)
Tasks.remove('Touch grass')
print("Updated list aftering removing 'Touch grass':", Tasks)
Tasks.pop(2)
print("Updated lists after popping the 2nd index || 'Read CB':", Tasks)
Tasks.append('Sell Puffco')
del Tasks[-1]
print('Updated list after using del to remove last index:', Tasks)
Tasks1 = [1,4,5,6,7,8,30,60] #Created for clear method, I require our first task list or 'Tasks' for our next exercise 
print('Dummy list:', Tasks1)
Tasks1.clear()
print('Updated list after clearing items from Tasks1:', Tasks1)

#Looping through lists
print("Tasks using a for loop:")
for item in Tasks:
    print(item) 

print('Tasks with indices using for loop:')
for item in range(len(Tasks)):
    print(f'{item}: {Tasks[item]}') # for items in range of the length(6) of our index: print the iteration number (index) and the corresponding item

print("Tasks printed using a while loop:")
item = 0
while item < len(Tasks):
    print(f'{item}:',Tasks[item])
    item = item + 1
#Loop through tasks, during iteration return items that are NOT 'Update Necessity List' if detected, replace w/ 'Modify Necessity List'
Tasks2 = [a if a != 'Update Necessity List' else 'Modify Necessity List' for a in Tasks]
print(Tasks2)
#Sort through list alphaebetically and print list!
Tasks.sort()
print('List after sorting alphabetically:', Tasks)

Tasks3 = Tasks.copy()
Tasks3.sort(reverse = True)
print("'Tasks' copied into our new task list dubbed 'Tasks3' in reverse order:", Tasks3)

print('Original task list to show nothing was altered after being copied to a different, new list.', Tasks)

Math = 800 * 8 - 4000 + 2 **16
Math1 = 45 - 800 + (9000/9) 
Math2 = 981 // 2 ** 4 - (8.8124124 % 2)

print('800 * 8 - 4000 + 2 **16 =', Math)
print('45 - 800 + (9000/9) =', Math1)
print('981 // 2 ** 4 - (8.8124124 % 2) =', int(Math2))
