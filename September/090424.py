#Exercise For loops and Conditionals 
#List of numbers from 1-20 | Print each number and its square, 
# but skip any numbers divisible by 4 + If square of a number greater than 150, stop loop

for num in range(1,21):
    if num % 4 == 0: ## If base number divisible by 4, skip to next num
        continue 
    square = num ** 2 
    if square >= 150: ## If square of num greater or equal to 150 stop loop. 
        break
    print(square) #Prints each square of num in range 1-20