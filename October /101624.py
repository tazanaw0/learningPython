#Exercise: Pizza Order Function 
# Create a Python function to simulate placing an order for a pizza. 

def order_pizza(pizza_type, *extratop, **delivery_info):
    toppings = ', '.join(extratop) if extratop else "No extra toppings." #Joins toppings into readable tuple(as opposed to outputting tuple syntax)
    print(f"So, you've ordered {pizza_type}, with the following extra toppings: {toppings}.")
    if delivery_info:
        print("Here are the details associated with your order:")
        for key, value in delivery_info.items(): #Outputs key:value pair on separate lines.
            print(f"{key.capitalize()}: {value}")
    else:
        print("No delivery details supplied with order.")

order_pizza("Cheese", "extra cheese", "green peppers", address = "123 Sally street, Omaha, Nebraska 11111", phone_num = '123-123-12345')
