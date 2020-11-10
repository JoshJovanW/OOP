from coffee import Coffee

class Macchiato(Coffee):
    def details(self):
        print("Made with vanilla syrup, steamed milk, espresso and caramel sauce. The espresso in poured on top of the milk leaving a dark mark on top of the milk foam")
 
    def add_topping(self, topping, price):
        if topping == "with extra jelly":
            raise Exception
        self.topping = topping
        self.price += price
