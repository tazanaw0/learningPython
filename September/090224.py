#(BRIEF)Exercise: Countdown timer 

starting_number = int(input('Enter starting number -> '))
# Takes input and checks 2 conditions, if divisible by 3, skip printing that num, amd if num <= 2 break the loop 
while starting_number > 0:
    if starting_number % 3 == 0:
        starting_number -=1
        continue 
    if starting_number <= 2:
        break 
    print(starting_number)
    starting_number -=1