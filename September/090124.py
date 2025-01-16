#Exercise: Custom Discount Calculator 
#Discount system based on customer's purchase amount for small e-comm platform

#Takes user input and saves it as an int as we are expecting users to enter a number (amount spent)
purchase_amount = float(input('Kindly type and enter in the amount you\'ve spent today: '))
originalPrice = purchase_amount ##Unnecessary, since we are not changing the var locally w/ in the if-else blocks
#Apply discount based on input 
twenty_discount = '20%'
ten_discount = '10%'
five_discount = '5%'
#Checks user input w/ 4 conditions, outputs their original price, the discount applied, and the final price after a discount is applied. 
if purchase_amount > 500:
    discount = purchase_amount * .20
    finalPrice = round(purchase_amount - discount, 2) 
    print(f'Original purchase amount -> ${originalPrice}')
    print('Discount applied ->', twenty_discount)
    print(f'Price w/ discount -> ${finalPrice}')
elif 200 <= purchase_amount <= 500:
    discount = purchase_amount * .10
    finalPrice = round(purchase_amount - discount, 2)
    print(f'Original purchase Amount -> ${originalPrice}')
    print('Discount applied ->', ten_discount)
    print(f'Price w/ discount -> ${finalPrice}')
elif 100 <= purchase_amount <= 199:
    discount = purchase_amount *.05
    finalPrice = round(purchase_amount - discount, 2)
    print(f'Original purchase amount -> ${originalPrice}') ### check to see if this outputs og price
    print('Discount applied ->', five_discount)
    print(f'Price w/ discount -> ${finalPrice}')
else:
    print('Your purchase doesn\'t qualify for a discount. Must be at least $100 spent :(')
