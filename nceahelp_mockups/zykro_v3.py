"""
Pizza order system
"""


def delivery():
    customer_name = input("What is the customer's name? ")
    customer_address = input("What is the customer's address? ")
    customer_phone = input("What is the customer's phone number? ")
    print("The total cost of the order is $", total_cost + 3)


def pickup():
    customer_name = input("What is the customer's name? ")
    amount_of_pizzas = int(input("How many pizzas would you like to order? "))
    # List of 12 pizzas, ordered.
    pizza_types = ["Pepperoni", "Cheese", "Hawaiian", "Meat Lovers", "Veggie", "Supreme", "BBQ Chicken",
               "Buffalo Chicken", "Chicken Alfredo", "Chicken Bacon Ranch", "Chicken Parmesan", "Chicken Ranch"]
    print("The pizza types available are: ")
    for pizza in pizza_types:
        print(pizza)
    pizza_order = input("What type of pizza would you like? ").lower().strip()
    if pizza_order in pizza_types:
        print("Your order has been placed.")
    else:
        print("Please enter a valid pizza type.")
        pickup()


def order_type():
    order_type = input("Is this a pickup or delivery order? ").lower().strip()
    if order_type == "pickup":
        pickup()
    elif order_type == "delivery":
        delivery()
    else:
        print("Please enter a valid order type.")
        order_type()



def main():



if __name__ == '__main__':
    main()
