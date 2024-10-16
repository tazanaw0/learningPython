#Exercise: Pizza Order Function 
# Create a Python function to simulate placing an order for a pizza. 

def order_pizza(pizza_type, *extratop, **delivery_info):
    print(f"So, you've ordered {pizza_type}, with the following extra toppings {extratop}.")
    print("Here are the details associated with your order", delivery_info)

order_pizza("Cheese", "extra cheese", "green peppers", address = "123 Sally st.", phone_num = '123-123-12345')
