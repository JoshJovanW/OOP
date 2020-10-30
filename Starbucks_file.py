#drink menu and price
def menu():
    print("Welcome to Starbucks at The Rocks \n")

    print("131 - 135 George Street, The Rocks,")
    print("Sydney, NSW 2000\n")

    print("Find us on George Street at the edgeof First Fleet Park & next door to ")
    print("Sydney's oldest pub, Fortune of War.\n")

    print("Sweét, Creämy and réfréshing\n")

    print("As of today there are 4 drinks available:\n ")

    print("- The Seasonal Lattes" + "      " + "- The Signature Frappucinos\n")
    
    print("- The Special Ice Coffees" + "  " + "- The Exquisite Macchiatos\n")

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
    print("MAKE IT YOURS?" + " " + "change milk (+2) " + " / " + "add 2 shots (+0.5) " + " / " + "Make skinny (+2) " + " / " + "less sugar (free) ")
    print("\n")
    print("* Don't forget to contact your barista if you have any allergies whatsoever.")



class Coffee:
    def __init__(self, price, size, topping, milk, amount, skinny, sugar):
        self.price = price
        self.size = size
        self.topping = topping
        self.milk = milk
        self.shots = amount
        self.skinny = skinny
        self.sugar = sugar

    def __str__(self):
        return f"This is the {self.name} with {self.topping} size {self.size} drink. It costs ${self.price}"

    def change_milk_to_almond(self,milk="Almond"):
        self.milk = milk
        self.price += 2

    def add_two_shots(self, amount="2"):
        self.shots = amount
        self.price += 0.5


    def make_skinny(self, skinny="Skinny"):
        self.skinny = skinny
        self.price += 2

    def less_sugar(self, sugar="less sugar"):
        self.sugar = sugar
    
        
        





class Latte(Coffee):
    def details():
        print("The layers of espresso and steamed milk are mixed together and topped with a light layer of foam. The drink is creamier and the coffee flavor is more subtle.")
        
    def latte_size_tall(self, size = "Tall", price = 4.25):
        self.size = size
        self.price = price

    def latte_size_grande(self, size = "Grande", price = 4.95):
        self.size = size
        self.price = price

    def latte_size_venti(self, size = "Venti", price = 5.25):
        self.size = size
        self.price = price
    
class Frappucino(Coffee):
    def details():
        print("It consists of coffee or crème base, blended with ice and other various ingredients, topped with whipped cream and flavored syrups")
        
    def frap_size_tall(self, size = "Tall", price = 3.45):
        self.size = size
        self.price = price

    def frap_size_grande(self, size = "Grande", price = 4.15):
        self.size = size
        self.price = price

    def frap_size_venti(self, size = "Venti", price = 4.45):
        self.size = size
        self.price = price

class IceCoffee(Coffee):
    def details():
        print("Freshly brewed Starbucks® Iced Coffee Blend served chilled and sweetened over ice. An absolutely, seriously, refreshingly lift to any day")

    def ice_size_tall(self, size = "Tall", price = 3.55):
        self.size = size
        self.price = price

    def ice_size_grande(self, size = "Grande", price = 4.25):
        self.size = size
        self.price = price

    def ice_size_venti(self, size = "Venti", price = 4.55):
        self.size = size 
        self.price = price

class Macchiato(Coffee):
    def details():
        print("Made with vanilla syrup, steamed milk, espresso and caramel sauce. The espresso in poured on top of the milk leaving a dark mark on top of the milk foam")
        
    def macchi_size_tall(self, size = "Tall", price = ):
        self.size = size
        self.price = price

    def macchi_size_grande(self, size = "Grande", price = ):
        self.size = size
        self.price = price

    def macchi_size_venti(self, size = "Venti", price = ):
        self.size = size 
        self.price = price



# bigger flow

menu()

price_Menu()

order_done = False

while order_done == False:
    print("Do you want to order? ")
    exit = input()

    if exit == "yes":
        print("what drink do you want to have? write like this: Latte or Macchiato")
        drink = input()
        if drink == "Latte":
            order1 = Latte(0, " ", None, None, None, None)
            print("what size do you want? *don't forget to write like the format before")
            latsize = input()

            if latsize == "Tall":
                order1.latte_size_tall()
                print("do you want to add a topping to your drink? type YES to continue.")
                answer = input()
                if answer == "YES":
                    print("what topping do you want to add? *type in the abbreviations for example ms for make skinny")
                    topping1 = input()
                    if topping1 == "ms":
                        order1.make_skinny()
                        print("do you want to add any other topping? write YES  to continue")
                        answer1 = input()
                        if answer1 = "YES":
                            print("what other topping do you want? ")
                            topping2 = input()
                            if topping2 == "as":
                                order1.add_two_shots()
                                print("do you want to add any other topping? type YES")
                                answer2 = input()
                                if answer2 == "YES":
                                    print("what do you want to add? ")
                                    topping3 = input()
                                    if topping3 == "cm":
                                        order1.change_milk_to_almond()
                                        print("do you want to add another topping? type YES to continue")
                                        answer3 = input()
                                        if answer3 = "YES":
                                            print("what do you want to add?")
                                            topping4 = input()
                                            if topping4 == "ls":
                                                order1.less_sugar()

                                            else:
                                                print("that topping is unavailable or have been chosen before")

                                        else:
                                            continue

                                    elif topping3 == "ls":
                                        print("do you want to add another topping? type YES to continue")
                                        answer3 = input()
                                        if answer3 = "YES":
                                            print("what do you want to add?")
                                            topping4 = input()
                                            if topping4 == "cm":
                                                order1.change_milk_to_almond()

                                    else:
                                        print("that topping is unavailable or have been chosen before")
                                
                                else:
                                    continue
                            
                            elif topping2 == "cm":
                                order1.change_milk_to_almond()
                                print("do you want to add any other topping? type YES")
                                answer2 = input()
                                if answer2 == "YES":
                                    print("what do you want to add? ")
                                    topping3 = input()
                                    if topping3 == "ls":
                                        order1.less_sugar()
                                        print("do you want to add another topping? type YES to continue")
                                        answer3 = input()
                                        if answer3 = "YES":
                                            print("what do you want to add?")
                                            topping4 = input()
                                            if topping4 == "as":
                                                order1.add_two_shots()
                                            
                                            else:
                                                print("that topping is unavailable or have been chosen before")

                                        else:
                                            continue 

                                    elif topping3 == as:
                                        order1.add_two_shots
                                        print("do you want to add another topping? type YES to continue")
                                        answer3 = input()
                                        if answer3 = "YES":
                                            print("what do you want to add?")
                                            topping4 = input()
                                            if topping4 == "ls":
                                                order1.less_sugar()

                                    else:
                                        print("that topping is unavailable or have been chosen before")
                                    
                            elif topping2 == "ls":
                                order1.less_sugar()
                                print("do you want to add any other topping? type YES")
                                answer2 = input()
                                if answer2 == "YES":
                                    print("what do you want to add? ")
                                    topping3 = input()
                                    if topping3 == "as":
                                        order1.change_milk_to_almond()
                                        print("do you want to add another topping? type YES to continue")
                                        answer3 = input()
                                        if answer3 = "YES":
                                            print("what do you want to add?")
                                            topping4 = input()
                                            if topping4 == "cm":
                                                order1.change_milk_to_almond()

                                            else:
                                                print("that topping is unavailable or have been chosen before")

                                        else:
                                            continue

                                    elif topping3 == "cm":
                                        order1.change_milk_to_almond
                                        print("do you want to add another topping? type YES to continue")
                                        answer3 = input()
                                        if answer3 = "YES":
                                            print("what do you want to add?")
                                            topping4 = input()
                                            if topping4 == "ls":
                                                order1.less_sugar()

                                    else:
                                        print("that topping is unavailable or have been chosen before")
                                
                    elif topping1 == "as":

            
                                
                                
                            

                            


 

                                

                                            


                        else:
                            continue



                else:
                    continue



            elif latsize == "Grande"

            elif latsize == "Venti"

        elif drink == "Frappucino":
            print("what size do you want? ")
            frapsize = input()

        elif drink == "Ice coffee":
            icesize = input()

        elif drink == "Macchiato":
            machisize = input()

        else:
            print("sorry this drink is not available.")


    else:
        print("Thank you for coming to starbucks")
        order_done = True

            
        









