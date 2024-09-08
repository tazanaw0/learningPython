#Exercise:if-else & for loops prac


#User input 
enter_num = int(input('Please enter a number between 1 and 50, then click enter -> '))

if enter_num > 50: #If users input greater than 50, we stop and print the error message to avoid iterations in for loop
    print('Number out of range, please enter a number between 1-50.')
else: 
    for i in range(enter_num): #iterate through each number in range of the users input 
        if i % 2 ==0: #Checks if num is even 
            print(f'Even:{i}')
        else: #If not even, must be odd
            print(f'Odd:{i}')

#Unnecessary iterations in for loop when number is greater than 50 
#for i in range(enter_num): #iterate through each number in range of the users input 
    #if enter_num > 50: #if user input greater than 50, prints 'error' message 
   #    print('Number out of range, please enter a number between 1-50.')
   #     break
   # elif i % 2 == 0: #If number evenly divisible by 2, print 'even' and the loops current iteration 
   #     print(f'Even:{i}')
   # elif i % 2 != 0: #If number is not evenly divisible by 2, print 'odd' and the loops current iteration. 
   #     print(f'Odd:{i}')
    