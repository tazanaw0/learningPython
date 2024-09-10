#Exercise: Countdown to 1
#Program that takes a user input and countdowns to one. Any number iterated that's divisible by 4, replace number with string. 

enter_num = int(input('Enter a number ->')) #Takes user input and stores it as an integer, as we're expecting user to input a number

if enter_num <= 0: 
    print('ERROR: MUST enter a number above 0.') #Outputs error message if user inputs negative number or 0 
else: 
    for item in range(enter_num, 0, -1): #(start, stop, step) 'step' tells the loop to begin at the end of the range
        if item % 4 == 0: #If divisible by 4, avoid printing the number, print 'Divisible by 4
            print('Divisible by 4')
        else:
            print(item)

