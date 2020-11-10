from coffee import Coffee

class Frappucino(Coffee):
    def details(self):
        print("It consists of coffee or crème base, blended with ice and other various ingredients, usually topped with whipped cream and flavored syrups")

    def add_topping(self, topping, price):
        if topping == "with extra jelly":
            raise Exception
        self.topping = topping
        self.price += price
