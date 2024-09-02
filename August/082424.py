#Exercise: Advanced Routine Management 
#Create a program that manages my routines, using methods like union, intersection and difference. 

#Initialize Data
morning_routine = {'Hygiene', 'Pray', 'Supplements', 'To-do list', 'Make food', 'Study for sec+'}
evening_routine = {'Study for sec+', 'Exercise', 'Python practice', 'Supplements', 
                   'Entertainment break', 'Make food'}
weekend_routine = ('Produce music', 'Cardio', 'Meal prep')

#Set Operations 
morning_evening_union = morning_routine | evening_routine #Returns new (joins) set with items from both sets
print(morning_evening_union)
morning_evening_intersect = morning_routine & evening_routine #Returns new (joins) set with items that are common between both sets
print(morning_evening_intersect)
morning_evening_diff = morning_routine - evening_routine #Returns new (joins) set with items that are unique in both sets 
print(morning_evening_diff) 

#Convert and update 
weekend_set = set(weekend_routine) #Convert tuple -> set
morning_routine.update(weekend_set) #Adds weekend (set) routines to morning routines
print('Result of updating our morning_routine set w/ weekend_routine ->', morning_routine)

#Final Adjustments
print('Popped item from morning_routine set ->', morning_routine.pop())
morning_routine.difference_update(weekend_set) #Removes weekend routine items that may be present in morning_routine
print('Removed items from morning_routine that appear in weekend_set ->', morning_routine) 

#Additional Challenge

daily_routine = morning_routine | evening_routine #Assigns or unions both morning and evening routines to one set 
print('Daily routines - >', daily_routine) 
#Convert daily_routine to list, so that we can use sort method to sort routines by alphabetical order
daily_routine_list = list(daily_routine)
daily_routine_list.sort()
print('Daily routine sorted ->', daily_routine_list)