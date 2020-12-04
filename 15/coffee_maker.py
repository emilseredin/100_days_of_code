class CoffeeMaker:

    def __init__(self, water, milk, coffee):
        self.water = water
        self.milk = milk
        self.coffee = coffee

    def get_report(self):
        return {
            "Water": self.water,
            "Milk": self.milk,
            "Coffee": self.coffee
        }

    def make(self, coffee, ingredients):
        if self.water < ingredients["water"]:
            return "Sorry, there is not enough water."
        elif self.coffee < ingredients["coffee"]:
            return "Sorry, there is not enough coffee."
        elif self.milk < ingredients["milk"]:
            return "Sorry, there is not enough milk."
        else:
            self.water = self.water - ingredients["water"]
            self.milk = self.milk - ingredients["milk"]
            self.coffee = self.coffee - ingredients["coffee"]
            return "Here is your {}. Enjoy!".format(coffee)

    def restock(self, water, milk, coffee):
        self.water += water
        self.milk += milk
        self.coffee += coffee
