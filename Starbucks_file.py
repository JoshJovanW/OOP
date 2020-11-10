# drink menu and price
from starbucks_menu_file import menu

from starbucks_price_file import price_Menu

from soylatte import SoyLatte

from frappucino import Frappucino

from icecoffee import IceCoffee

from macchiato import Macchiato




# bigger flow

receipt = 0

menu()

price_Menu()

orders = []

order = None

finished = False



while finished == False:
    print("what do you want to order? Type SL for Soy Latte , JCF for Java chip Frappucino, ICJ for Ice Coffe Jelly and CM for Caramel macchiato")
    answer = input()
    if answer == "SL":
        order = SoyLatte("soy latte", 4.25, "tall", "normal", "without topping")
    
    elif answer == "JCF":
        order = Frappucino("java chip frappucino", 3.45, "tall", "normal", "without topping")

    elif answer == "ICJ":
        order = IceCoffee("ice coffee jelly", 3.55, "tall", "normal", "without topping")

    elif answer == "CM":
        order = Macchiato("caramel macchiato", 4.99, "tall", "normal", "without topping")

    print("do you want your drink to be less sugar or normal? ")
    sugar = input()

    if sugar == "less":
        order.less_sugar()

    else:
        pass

    print("what size do you want? Type T for Tall, G for Grande, V for Venti. ")
    size = input()

    if size == "T":
        order.change_size(0, "Tall")

    elif size == "G":
        order.change_size(0.7, "Grande")

    elif size == "V":
        order.change_size(1, "Venti")

    print("do you want to add topping for your coffee? Type Yes. *some toppings are not available for specific drinks")
    boolean = input()
    if boolean == "Yes":
        print("Which topping do you want? Type AS to add extra 2 shots, WC for extra Whip Cream, J for extra Jelly and CF for extra Cloud Foam. ")
        topping = input()

        if topping == "AS":
            order.add_topping("with 2 extra shots", 0.5)

        elif topping == "J":
            order.add_topping("with extra jelly", 2)

        elif topping == "WC":
            order.add_topping("with extra whip cream", 2)
    
        elif toppping == "CF":
            order.add_topping("with extra cloud foam", 1)

    orders.append(order)
    print("do you want to order another drink?Type Yes to continue ")
    another = input()

    if another == "Yes":
        pass

    else:
        finished = True


else:
    for idx, value in enumerate(orders):
        receipt += orders[idx].price

    print(f"heres your total bill ${receipt}")

    print("what do you want to pay with (Cash / Credit) ? *if you use credit card you will get a 20 percent discount\n")

    print("Type 'CASH' for Cash and 'CREDIT' for Credit")

    payment = input()

    if payment == "CASH":
        print("How much Dollars do you want to give? ")
        dollars = float(input())

        print(f"Here's your change. ${round((dollars - receipt), 2)}")

    elif payment == "CREDIT":
        print(f"Your final cost will be ${round((receipt/100 * 80), 2)}")

    print("thank you for ordering at starbucks")



          



        









