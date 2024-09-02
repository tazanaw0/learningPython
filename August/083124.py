#Exercise: Decision-Making w/ if-else
#Outfit recommendation program that suggest what to wear based on temps

#Initializing Variables (temp in degrees Fahrenheit)
temp = 72 

#Decision-making using if-else

if temp == 72:
    print('Perfect weather today! Wear shorts and a tank.')
elif temp > 80:
    print("It's hot outside, wear shorts and a t-shirt")
elif 60 < temp <= 80:
    print("It's warm outside, wear light clothing.")
elif 40 <= temp <=59:
    print("It's a bit chilly, wear a jacket.")
else:
    print("It's cold outside, wear a coat and warm clothing.")
