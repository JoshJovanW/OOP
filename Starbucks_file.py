def menu():
    print("Welcome to Starbucks at The Rocks \n")

    print("131 - 135 George Street, The Rocks,")
    print("Sydney, NSW 2000\n")

    print("Find us on George Street at the edgeof First Fleet Park & next door to ")
    print("Sydney's oldest pub, Fortune of War.\n")

    print("Sweét, Creämy and réfréshing\n")

    print("As of today there are 4 drinks available:\n ")

    print("- The Seasonal Soy Lattes" + "      " + "- The Signature Java Chip Frappucinos\n")
    
    print("- The Special Almond Ice Coffees" + "  " + "- The Exquisite Caramel Macchiatos\n")

    print("\n")

    print("To find out more about the drinks read the information below: \n")



def price_Menu():
    print("The prices are listed below: \n") 
   
    #Latte prices
    print("Lattes"  +  "          "  + "Tall  " +    "    "  +  "$4.25\n")
    print("Lattes"  +  "          "  + "Grande" +  "    "  + "$4.95\n")
    print("Lattes"  +  "          "  + "Venti " +   "    " + "$5.25\n")

    #Frappucino prices
    print("Frappucino"  +  "      "  + "Tall  "  +   "    "  +  "$3.45\n")
    print("Frappucino"  +  "      "  + "Grande"  + "    "  +  "$4.15\n")
    print("Frappucino"  +  "      "  + "Venti "  +  "    "  +  "$4.45\n")

    #Ice Coffee prices
    print("Ice Coffee"  +  "      "  + "Tall  " +    "    "  + "$3.55\n")
    print("Ice Coffee"  +  "      "  + "Grande" +  "    "  + "$4.25\n")
    print("Ice Coffee"  +  "      "  + "Venti " +   "    "  +  "$4.55\n")
 
    #Macchiato prices
    print("Macchiatos"  +  "      "  + "Tall  " +    "    "  + "$4.99\n")
    print("Macchiatos"  +  "      "  + "Grande" +  "    " + "$5.69\n")
    print("Macchiatos"  +  "      "  + "Venti " +   "    " + "$5.99\n") 

    #TOPPING PRICES
    print("MAKE IT YOURS?" + " " + "add jelly(+2) * only for ice coffee " + " / " + "add 2 shots(+0.5) *only for latte " + " / " + "whip cream (+2)*only for java chip frappucino " + " / " + "cloud foam (+1) *only for macchiato " + "less sugar (free) ")
    print("\n")
    print("* Don't forget to contact your barista if you have any allergies whatsoever.\n")


class Coffee:
    def __init__(self, name, price, size, sugar, topping):
        self.name = name
        self.price = price
        self.size = size
        self.sugar = sugar
        self.topping = topping

    def __str__(self):
        return f"You ordered the {self.name} with {self.sugar} sugar, {self.topping}, size {self.size} drink. It costs ${self.price}"

    def less_sugar(self, sugar="less"):
        self.sugar = sugar

    def change_size(self, price, size):
        self.price = price
        self.size = size

    def add_topping(self, topping, price):
        self.topping = topping
        self.price += price


class SoyLatte(Coffee):
    def details(self):
        print("The layers of espresso and steamed milk are mixed together and topped with a light layer of foam. The drink is creamier and the coffee flavor is more subtle.")

    def add_topping(self, topping, price):
        if topping == "with extra cloud foam":
            raise Exception
        self.topping = topping
        self.price += price


class Frappucino(Coffee):
    def details(self):
        print("It consists of coffee or crème base, blended with ice and other various ingredients, usually topped with whipped cream and flavored syrups")

    def add_topping(self, topping, price):
        if topping == "with extra jelly":
            raise Exception
        self.topping = topping
        self.price += price


class IceCoffee(Coffee):
    def details(self):
        print("Freshly brewed Starbucks® Iced Coffee Blend served chilled and sweetened over ice. An absolutely, seriously, refreshingly lift to any day")

    def add_topping(self, topping, price):
        if topping == "with extra whip cream":
            raise Exception
        self.topping = topping
        self.price += price
    
class Macchiato(Coffee):
    def details(self):
        print("Made with vanilla syrup, steamed milk, espresso and caramel sauce. The espresso in poured on top of the milk leaving a dark mark on top of the milk foam")
 
    def add_topping(self, topping, price):
        if topping == "with extra jelly":
            raise Exception
        self.topping = topping
        self.price += price


menu()

price_Menu()


order1 = None

print("what do you want to order? Type SL for Soy Latte , JCF for Java chip Frappucino, ICJ for Ice Coffe Jelly and CM for Caramel macchiato")
if answer == "SL":
    order1 = SoyLatte("soy latte", 4.25, "tall", "normal", "without topping")
    
elif answer == "java chip frappucino":
    order1 = Frappucino("java chip frappucino", 3.45, "tall", "normal", "without topping")

elif answer == "ice coffee jelly":
    order1 = IceCoffee("ice coffee jelly", 3.55, "tall", "normal", "without topping")

elif answer == "caramel macchiato":
    order1 = Macchiato("caramel macchiato", 4.99, "tall", "normal", "without topping")

print("do you want your drink to be less sugar or normal? ")
sugar = input()

if sugar == "less":
    order1.less_sugar()

else:
    pass

print("what size do you want? Type T for Tall, G for Grande, V for Venti. ")
size = input()

if size == "T":
    order1.change_size(0, "Tall")

elif size == "G":
    order1.change_size(0.7, "Grande")

elif size == "V":
    order1.change_size(0.3, "Venti")

print("do you want to add topping for your coffee? Type Yes. *some toppings are not available for specific drinks")
boolean = input()
if boolean == "Yes":
    print("Which topping do you want? Type AS to add extra 2 shots, WC for extra Whip Cream, J for extra Jelly and CF for extra Cloud Foam. ")
    topping = input()

    if topping == "AS":
        order1.add_topping("with 2 extra shots", 0.5)

    elif topping == "J":
        order1.add_topping("with extra jelly", 2)

    elif topping == "WC":
        order1.add_topping("with extra whip cream", 2)
    
    elif toppping == "CF":
        order1.add_topping("with extra cloud foam", 1)


          
