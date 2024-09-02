#Exercise: Data Manipulation and Arithmetic Operations 
#Defining our global variables 
num = 9 
num2 = 3
num3 = 2
floaty = 10.14214
words1 = 'Now playing:'
words = 'Willpower x Mavi'
WORDS = 'Got me hyped ngl'
cool = True
cool1 = False
cool2 = True

print(num + num2) # Addition operator 
print(num - num2) # Subtraction Operator 
print(num * num2) # Multiplication Operator 
print(num / num2) # Division Operator 
print(num % num3) # Modulus Operator 
print(len(words)) #Length function used to print number of characters in string 
print(words.upper()) #Converts 'words' string to all uppercase letters 
print(words1 + " " + words) # Concatenates our words global var with WORDS + I inculded a space for readability 
print('cool and cool1:', cool and cool1) #Boolean and opeartor 
print('cool1 or cool2:', cool1 or cool2) #Boolean or operator 
print('not cool1:', not cool1) #Boolean not operator 
print('Float to int:', int(floaty)) #Casting an float variable to a integer 
print('Int to float:', float(num2)) #Casting an integer variable to a float 