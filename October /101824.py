#Exercise: Calculate Total Price
def calculate_total(price, quantity, /, *, discount = 0):
   return price * quantity - discount


print(calculate_total(50, 5, discount = 40))
print(calculate_total(100, 8, discount = 75))
#print(calculate_total(500,5, discount = .50))
  #discount_applied = (price * quantity) * discount
    #total_price = price - discount_applied
    #return total_price