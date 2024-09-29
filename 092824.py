#Exercise: Check for even or odd numbers

#Asks the user to input a number between 1 and 100.
##Checks if the number is even or odd.
###Prints whether the number is even or odd

#
users_number = int(input('Please enter a number between 1 and 100: '))

##
if users_number % 2 == 0:
    print('Even')
else:
    print('Odd')