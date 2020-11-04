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
    def __init__(self, name, price, size, sugar):
        self.name = name
        self.price = price
        self.size = size
        self.sugar = sugar

    def __str__(self):
        return f"You ordered the {self.name} with {self.sugar} sugar, size {self.size} drink. It costs ${self.price}"

    def less_sugar(self, sugar="less"):
        self.sugar = sugar

    def change_size(self, price, size):
        self.price = price
        self.size = size


class SoyLatte(Coffee):
    def __init__(self, name, price, size, sugar, shots):
        Coffee.__init__(self, name, price, size, sugar)
        self.shots = shots

    def details(self):
        print("The layers of espresso and steamed milk are mixed together and topped with a light layer of foam. The drink is creamier and the coffee flavor is more subtle.")

    def add_extra_shots(self):
        self.shots = "2 extra"
        self.price += 0.5

    def __str__(self):
        return f"You ordered the {self.name} with {self.sugar} sugar, with {self.shots} shots, size {self.size} drink. It costs ${self.price}"


class Frappucino(Coffee):
    def __init__(self, name, price, size, sugar, cream):
        Coffee.__init__(self, name, price, size, sugar)
        self.cream = cream

    def details(self):
        print("It consists of coffee or crème base, blended with ice and other various ingredients, usually topped with whipped cream and flavored syrups")

    def add_cream(self):
        self.cream = "with"
        self.price += 2

    def __str__(self):
        return f"You ordered the {self.name} with {self.sugar} sugar, {self.cream} whip cream, size {self.size} drink. It costs ${self.price}"


class IceCoffee(Coffee):
    def __init__(self, name, price, size, sugar, jelly):
        Coffee.__init__(self, name, price, size, sugar)
        self.jelly = jelly

    def details(self):
        print("Freshly brewed Starbucks® Iced Coffee Blend served chilled and sweetened over ice. An absolutely, seriously, refreshingly lift to any day")

    def add_jelly(self):
        self.jelly = "with"
        self.price += 2

    def __str__(self):
        return f"You ordered the {self.name} with {self.sugar} sugar, {self.jelly} extra jelly, size {self.size} drink. It costs ${self.price} "


class Macchiato(Coffee):
    def __init__(self, name, price, size, sugar, foam):
        Coffee.__init__(self, name, price, size, sugar)
        self.foam = foam

    def details(self):
        print("Made with vanilla syrup, steamed milk, espresso and caramel sauce. The espresso in poured on top of the milk leaving a dark mark on top of the milk foam")
        
    def add_foam(self):
        self.foam = "with"
        self.price += 1

    def __str__(self):
        return f"You ordered the {self.name} with {self.sugar} sugar, {self.foam} extra foam, size {self.size} drink. It costs ${self.price}"
    
    
# bigger flow

menu()

price_Menu()

print("what do you want to order? Write 'soy latte' for the soy latte, 'java chip frappucino' for the java chip frappucino , 'almond ice coffee' for the almond ice coffee, 'caramel macchiato' for the caramel macchiato")

answer = input()

if answer == "soy latte":
    order1 = SoyLatte("soy latte", 4.25, "tall", "Normal", "Normal")
    print("Do you want to find out about the details of this drink? Type yes to find out")
    input1 = input()
    if input1 == "yes":
        order1.details()
    else:
        pass
    
    print("what size do you want?")
    size = input()
    if size == "tall":
        print("do you want to add a topping? type yes to continue")
        boolean = input()

        if boolean == "yes":
            print("do you want to add extra shots for your latte? type yes if you want")
            shots = input()
            if shots == "yes":
                order1.add_extra_shots()
                print("Less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

            else:
                print("less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

        else:
            print("less sugar or normal?")
            sugar = input()
            if sugar == "less":
                order1.less_sugar()
                print(order1)

            else:
                print(order1)

    elif size == "grande":
        order1.change_size(4.95, "Grande")
        print("do you want to add a topping? type yes to continue")
        boolean = input()

        if boolean == "yes":
            print("do you want to add extra shots for your latte? type yes if you want")
            shots = input()
            if shots == "yes":
                order1.add_extra_shots()
                print("Less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

            else:
                print("less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

        else:
            print("less sugar or normal?")
            sugar = input()
            if sugar == "less":
                order1.less_sugar()
                print(order1)

            else:
                print(order1)


    elif size == "venti":
        order1.change_size(5.25, "Venti")
        print("do you want to add a topping? type yes to continue")
        boolean = input()

        if boolean == "yes":
            print("do you want to add extra shots for your latte? type yes if you want")
            shots = input()
            if shots == "yes":
                order1.add_extra_shots()
                print("Less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

            else:
                print("less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

        else:
            print("less sugar or normal?")
            sugar = input()
            if sugar == "less":
                order1.less_sugar()
                print(order1)

            else:
                print(order1)

elif answer == "java chip frappucino":
    order1 = Frappucino("java chip frappucino", 3.45, "tall", "Normal", "without")
    print("Do you want to find out about the details of this drink? Type yes to find out")
    input1 = input()
    if input1 == "yes":
        order1.details()
    else:
        pass
    
    print("what size do you want?")
    size = input()
    if size == "tall":
        print("do you want to add a topping? type yes to continue")
        boolean = input()

        if boolean == "yes":
            print("do you want to add extra whip cream for your Frappucino? type yes if you want")
            cream = input()
            if cream == "yes":
                order1.add_cream()
                print("Less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

            else:
                print("less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

        else:
            print("less sugar or normal?")
            sugar = input()
            if sugar == "less":
                order1.less_sugar()
                print(order1)

            else:
                print(order1)

    elif size == "grande":
        order1.change_size(4.15, "Grande")
        print("do you want to add a topping? type yes to continue")
        boolean = input()

        if boolean == "yes":
            print("do you want to add extra whip cream for your Frappucino? type yes if you want")
            cream = input()
            if cream == "yes":
                order1.add_cream()
                print("Less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

            else:
                print("less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

        else:
            print("less sugar or normal?")
            sugar = input()
            if sugar == "less":
                order1.less_sugar()
                print(order1)

            else:
                print(order1)

    elif size == "venti":
        order1.change_size(4.45, "Venti")
        print("do you want to add a topping? type yes to continue")
        boolean = input()

        if boolean == "yes":
                print("do you want to add extra whip cream for your Frappucino? type yes if you want")
                cream = input()
                if cream == "yes":
                    order1.add_cream()
                    print("Less sugar or normal?")
                    sugar = input()
                    if sugar == "less":
                        order1.less_sugar()
                        print(order1)

                    else:
                        print(order1)

                else:
                    print("less sugar or normal?")
                    sugar = input()
                    if sugar == "less":
                        order1.less_sugar()
                        print(order1)

                    else:
                        print(order1)

        else:
            print("less sugar or normal?")
            sugar = input()
            if sugar == "less":
                order1.less_sugar()
                print(order1)

            else:
                print(order1)

elif answer == "almond ice coffee":
    order1 = IceCoffee("almond ice coffee", 3.55, "tall", "Normal", "without")
    print("Do you want to find out about the details of this drink? Type yes to find out")
    input1 = input()
    if input1 == "yes":
        order1.details()
    else:
        pass
    
    print("what size do you want?")
    size = input()
    if size == "tall":
        print("do you want to add a topping? type yes to continue")
        boolean = input()

        if boolean == "yes":
            print("do you want to add extra jelly for your ice coffee? type yes if you want")
            jelly = input()
            if jelly == "yes":
                order1.add_jelly()
                print("Less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

            else:
                print("less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

        else:
            print("less sugar or normal?")
            sugar = input()
            if sugar == "less":
                order1.less_sugar()
                print(order1)

            else:
                print(order1)

    elif size == "grande":
        order1.change_size(4.25, "Grande")
        print("do you want to add a topping? type yes to continue")
        boolean = input()

        if boolean == "yes":
            print("do you want to add extra jelly for your latte? type yes if you want")
            jelly = input()
            if jelly == "yes":
                order1.add_jelly()
                print("Less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

            else:
                print("less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

        else:
            print("less sugar or normal?")
            sugar = input()
            if sugar == "less":
                order1.less_sugar()
                print(order1)

            else:
                print(order1)


    elif size == "venti":
        order1.change_size(4.55, "Venti")
        print("do you want to add a topping? type yes to continue")
        boolean = input()

        if boolean == "yes":
            print("do you want to add extra jelly for your latte? type yes if you want")
            jelly= input()
            if jelly == "yes":
                order1.add_jelly()
                print("Less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

            else:
                print("less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

        else:
            print("less sugar or normal?")
            sugar = input()
            if sugar == "less":
                order1.less_sugar()
                print(order1)

            else:
                print(order1)

elif answer == "caramel macchiato":
    order1 = Macchiato("caramel macchiato", 4.99, "tall", "Normal", "without")
    print("Do you want to find out about the details of this drink? Type yes to find out")
    input1 = input()
    if input1 == "yes":
        order1.details()
    else:
        pass
    
    print("what size do you want?")
    size = input()
    if size == "tall":
        print("do you want to add a topping? type yes to continue")
        boolean = input()

        if boolean == "yes":
            print("do you want to add extra cloud foam for your ice coffee? type yes if you want")
            foam = input()
            if foam == "yes":
                order1.add_foam()
                print("Less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

            else:
                print("less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

        else:
            print("less sugar or normal?")
            sugar = input()
            if sugar == "less":
                order1.less_sugar()
                print(order1)

            else:
                print(order1)

    elif size == "grande":
        order1.change_size(5.69, "Grande")
        print("do you want to add a topping? type yes to continue")
        boolean = input()

        if boolean == "yes":
            print("do you want to add extra cloud foam for your ice coffee? type yes if you want")
            foam = input()
            if foam == "yes":
                order1.add_foam()
                print("Less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

            else:
                print("less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

        else:
            print("less sugar or normal?")
            sugar = input()
            if sugar == "less":
                order1.less_sugar()
                print(order1)

            else:
                print(order1)

       

    elif size == "venti":
        order1.change_size(5.99, "Venti")
        print("do you want to add a topping? type yes to continue")
        boolean = input()

        if boolean == "yes":
            print("do you want to add extra cloud foam for your ice coffee? type yes if you want")
            foam = input()
            if foam == "yes":
                order1.add_foam()
                print("Less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

            else:
                print("less sugar or normal?")
                sugar = input()
                if sugar == "less":
                    order1.less_sugar()
                    print(order1)

                else:
                    print(order1)

        else:
            print("less sugar or normal?")
            sugar = input()
            if sugar == "less":
                order1.less_sugar()
                print(order1)

            else:
                print(order1)





        







