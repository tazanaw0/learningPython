#Exercise: Personal Info Summary (GPT)
#Creating a pgoram that collects and summarizes personal information 

#Defining Variables and their respective data types
first_name = str('Temesgen')
last_name = str('Azanaw')
age = int(24)
height = float(1.88)
is_student = bool(True)
weight = float(175)
weights = f'{weight} lbs.'
fav_color = str('blue')

#Arithmetic Operations 
age_in_months = 24 * 12
print('This student is:', age_in_months, 'months old.') #f string would've looked cleaner here
height_in_cm = height * 100
print('This student is:', height_in_cm, 'cm tall.')

#String Operations
full_name = first_name + " " + last_name
print('The student\'s full name is:', full_name)
print('Full name in uppercase:', full_name.upper())
print('Length of full name:', len(full_name))
checkChar = 'b' in full_name
print('Contains \'b\':', checkChar) #False
current_weight = f'Temesgen currently weights {weights}' 

#Boolean Operations
is_adult = age >= 18 #True
print('Adult and student:', is_adult and is_student) #True
print('An adult or student:', is_adult or is_student) #True

#Casting
metersToInt = int(height)
print('Height as integer:', metersToInt)
AgeToFloat = float(age)
print('Age as float:', AgeToFloat)
age_to_string = str(age)
output_age = str(f'The student is {age_to_string} years old.')
print(output_age)
print(current_weight)
#Reversed String
reverse = current_weight [::-1] #Slices the string from the end || backwards
print(reverse)