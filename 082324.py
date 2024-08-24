#Exercise: Routine Management w/ Sets and Tuples (GPT)
#Create a program that manages your routines. Working w/ adding, removing, and manipulating data in sets and tuples

#Initializing Data | Second set should have  a few items that overlap w/ the first
morning_routine = {'Pray', 'Hygiene', 'Eat', 'Check to-do list', 'Study for Sec+'}
evening_routine = {'Learn python through w3 schools', 'Watch a show', 'Make tea', 'VS for python practice', 'Eat'}
weekend_activities = ('Binge tv', 'Practice w/ python', 'Produce music')

#Manipulating sets 
morning_routine.add('Exercise')
morning_routine.add('Make caffeinated bev')
print(morning_routine)

evening_routine.remove('Make tea')
evening_routine.discard('Watch a show')

print(morning_routine.pop())

#Converting and updating
weekend_set = set(weekend_activities)
morning_routine.update(weekend_set)
print('Updated morning routine set after adding our weekend activities', morning_routine)

weekend_set.clear()
print('Weekend_set post clear method ->', weekend_set)
del weekend_set
