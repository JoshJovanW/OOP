from coffee import Coffee

class IceCoffee(Coffee):
    def details(self):
        print("Freshly brewed Starbucks® Iced Coffee Blend served chilled and sweetened over ice. An absolutely, seriously, refreshingly lift to any day")

    def add_topping(self, topping, price):
        if topping == "with extra whip cream":
            raise Exception
        self.topping = topping
        self.price += price
