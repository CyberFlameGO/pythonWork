"""
Pizza order system.
Final output is given in order of importance instead of order of input (i.e. order details, type of order, then
customer info, instead of order type, customer info, then order details)

Features not implemented: format conformity checking for phone numbers and addresses
"""


def integer_input_check(query):
    while True:
        try:
            return int(input(query).strip())
        except ValueError:
            print("Please enter a valid integer.")


def order(delivery_order = False):
    """
    :param delivery_order: Whether or not the order is a delivery order
    """
    # List of 12 pizzas, ordered.
    regular_pizzas = ["Pepperoni", "Cheese", "Hawaiian", "Meat Lovers", "Veggie", "Supreme", "BBQ Chicken"]
    gourmet_pizzas = ["Buffalo Chicken", "Chicken Alfredo", "Chicken Bacon Ranch", "Chicken Parmesan", "Chicken Ranch"]
    extra_toppings = 0  # Tracks whether the customer wants more of a pizza topping for the pizza they're ordering
    ordered_pizzas = []
    total_cost = 0
    print("The pizza types available are as follows: "
          "\n Regular ($8.50): ")
    for pizza in regular_pizzas:
        print("  -  " + pizza)
    print(" Gourmet ($13.50): ")
    for pizza in gourmet_pizzas:
        print("  -  " + pizza)
    print("Having extra toppings are 50¢ per pizza (will be rolled into pizza price).")

    amount_of_pizzas = integer_input_check("How many pizzas would they like to order? (max. 5)\nAmount: ")
    for pizza in range(amount_of_pizzas):
        validity_check = True

        while validity_check:
            pizza_order = input("What type of pizza would they like? ").title().strip()
            if pizza_order in [*regular_pizzas, *gourmet_pizzas]:
                if input("Extra toppings? y/other\nInput: ").lower().strip() == "y":
                    extra_toppings += 1
                    ordered_pizzas.append(pizza_order + "*")
                else:
                    ordered_pizzas.append(pizza_order)
                print("Pizza has been added to order")
                validity_check = False
            else:
                print("Please enter a valid pizza type.")
    print("Order is as follows: ")
    for pizza in ordered_pizzas:
        pizza_cost = 0
        if pizza.endswith("*"):
            if pizza[:-1] in regular_pizzas:
                pizza_cost = 9
                total_cost += pizza_cost
            else:
                pizza_cost = 14
                total_cost += pizza_cost
            pizza = pizza.replace("*", " with extra toppings")
        else:
            if pizza in regular_pizzas:
                pizza_cost = 8.5
                total_cost += pizza_cost
            else:
                pizza_cost = 13.5
                total_cost += pizza_cost
        print(" - " + "${:,.2f}".format(pizza_cost),  pizza)
    if delivery_order:
        print("Delivery fee: $3.00")
        total_cost += 3
    print("Total cost: $" + "{:,.2f}".format(total_cost))


def delivery():
    unconfirmed = True  # Recycled variable for the confirmation of customer information

    customer_name = input("What is the customer's name? ").title().strip() + "."  # Something this trivial doesn't
    # need as
    # much
                                                                          # accuracy as a phone number or address

    while unconfirmed:
        customer_address = input("What is the customer's address? ")
        if input("Is this correct? (y/other) \n" + customer_address + "\nAnswer: ").lower().strip() == "y":
            unconfirmed = False
    unconfirmed = True
    while unconfirmed:
        # This is a string because + and # may be used in phone numbers.
        customer_phone = input("What is the customer's phone number? ")
        if input("Is this correct? (y/other) \n" + customer_phone + "\nAnswer: ").lower().strip() == "y":
            unconfirmed = False
    order(True)
    return customer_name, customer_address, customer_phone


def pickup():
    customer_name = input("What is the customer's name? ").title().strip() + "."
    order()
    return customer_name


def order_type():
    deliver = False
    checking = True
    while checking:
        order_type = input("Is this a pickup or delivery order? ").lower().strip()
        if order_type == "pickup":
            checking = False
            name = pickup()
            print("Customer name: " + name)
        elif order_type == "delivery":
            checking = False
            deliver = True
            info = delivery()
            print("Customer name: " + info[0])
            print("Customer address: " + info[1])
            print("Customer phone number: " + info[2])
        else:
            print("Please enter a valid order type.")
    return deliver


def main():
    while True:
        print("Remember: At any time, you may cancel the order by pressing Ctrl+C in the input box "
              "(this will stop the program)")
        print("Order type: " + ("Delivery" if order_type() else "Pickup"))
        if input("Would you like to place another order? Type 'n' if not, "
                 "or anything else if so. ").lower().strip() == "n":
            return


if __name__ == '__main__':
    main()
