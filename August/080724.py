#Excerise: Basic Data Handling and Operations (Courtesy of ChatGpt)

#Global Variables of different data types 
num = int(25)
floaty = float(3.33)
hows_your_day = str('I\'ve had a great, productive and successful day.'); 
Bool = bool(True)
ComplexDataType = complex(floaty)

#Simple Arithmetic Operations
simple_add = num + floaty
simple_subtract = num - floaty
simple_multiply = num * floaty
simple_divide = num / floaty
simple_mod = num % floaty

#output answers to console 
print(simple_add)
print(simple_subtract)
print(simple_multiply)
print(simple_divide)
print(simple_mod)

#String Operations 
consistent = 'I will continue as I\'ve been very consistent.'
print(len(hows_your_day))
print(hows_your_day[5:]) #Output = 'had a great...
print(hows_your_day.upper())
print(hows_your_day + " " + consistent)

#Boolean Operations
Bool1 =bool(False)
Bool2 = bool(True)
Bool3 = bool(False)
#Combining the booleans with logical operators :)
print('Bool and Bool1:', bool and Bool1)#False
print('Bool1 or Bool2:', Bool1 or Bool2)#True
print('not Bool3:', not Bool3) # True

#Casting 
print(int(floaty))
print(float(num))
concatenated = str(num)
print('Num casted to string:', concatenated)

#Test 
print(ComplexDataType)