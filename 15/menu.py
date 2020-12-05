class MenuItem:

    def __init__(self, water, milk, coffee, cost):
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
        self.cost = cost

    def get_ingredients(self):
        return self.ingredients

    def get_cost(self):
        return self.cost



class Menu:

    def __init__(self):
        self.menu = {
            "espresso": MenuItem(water=50, milk=0, coffee=18, cost=1.5),
            "latte": MenuItem(water=200, milk=150, coffee=24, cost=2.5),
            "cappuccino": MenuItem(water=250, milk=100, coffee=24, cost=3.0)
        }

    def get_ingredients(self, coffee):
        if coffee in self.menu:
            return self.menu[coffee].get_ingredients()

    def get_price(self, coffee):
        if coffee in self.menu:
            return self.menu[coffee].get_cost()

    def get_items(self):
        return self.menu.keys()
