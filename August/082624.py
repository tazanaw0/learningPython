#Exercise: Dictionary Basics (Short)
#Quick exercise to reinforce understanding of dictionaries 

#Initializing Dictionary 
student_info = {
    'name' : 'Teme',
    'age' : 24,
    'courses' : ['SCIA 460', 'Graphic Design', 'w3 Python']
}
#Verifying list creation
print(type(student_info['courses']))

#Access and modify
name = student_info.get('name') 
print('Accessing our name by using .get() method ->', name)
print('Accessing our name by referring to key name ->', student_info['name']) 
#adding new key value pair
student_info['grade_level'] = 'Senior'
print('Updated dict w/ new key dubbed \'grade_level\' ->', student_info)
#Increasing our age by 1 using update method
student_info.update({'age':25})
print('Updated dict after modifying our age by +1 ->', student_info)

#Remove and print
del student_info['courses']
print('Updated dict following the removal of \'courses\' key ->', student_info)
