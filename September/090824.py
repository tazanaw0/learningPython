#Exercise: Divisible by 3 and 5 
#Takes user input between a range of 1 & 100, then use a loop to print every number up to that input
#If input divisible by 3 print 'Fizz' | If divisible by 5 print 'buzz' | If input divisible by both 3 & 5 print 'FizzBuzz,' otherwise just print the number 

user_input = int(input('Please enter a number between 1 & 100 ->'))

if user_input > 100:
    print('Sorry, you MUST enter a number between 1 and 100.')
else:
    for i in range(1, user_input + 1): #For each number leading up to users input, + 1 so we make sure to include the users input i
        if i % 3 == 0 and i % 5 == 0: # if divisible by 3 and 5 print the iteration w/ 'fizzbuzz'
            print(f'{i}-> FizzBuzz')
        elif i % 3 == 0: #If only divisible by 3 print 'fizz'
            print(f'{i} -> Fizz')
        elif i % 5 == 0: #if only divisible by 5 print 'buzz'
            print(f'{i} -> Buzz')
        else:
            print(i)
        