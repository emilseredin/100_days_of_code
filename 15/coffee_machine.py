from menu import Menu
from cache_registry import CacheRegistry


class CoffeeMachine:

    def __init__(self, water, milk, coffee):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cache_registry = CacheRegistry()
        self.menu = Menu()
        self.running = False

    def get_report(self):
        return "Water: {}ml\nMilk: {}ml\nCoffee: {}\nMoney: {}".format(
            self.water, self.milk, self.coffee, self.cache_registry.get_money())

    def restock(self, water, milk, coffee):
        self.water += water
        self.milk += milk
        self.coffee += coffee

    def make(self, coffee):
        ingredients = self.menu.get_ingredients(coffee)
        price = self.menu.get_price(coffee)
        if self.water < ingredients["water"]:
            print("Sorry, there is not enough water.")
        elif self.coffee < ingredients["coffee"]:
            print("Sorry, there is not enough coffee.")
        elif self.milk < ingredients["milk"]:
            print("Sorry, there is not enough milk.")
        else:
            print("{} costs ${}".format(coffee.capitalize(), price))
            complete, change = self.cache_registry.check_transaction(
                cost=price)
            if change:
                print("Here is ${} in change.".format(change))
            if complete:
                self.water = self.water - ingredients["water"]
                self.coffee = self.coffee - ingredients["coffee"]
                print("Here is your {}. Enjoy!".format(coffee))
            else:
                print("Sorry, that's not enough money. Money refunded.")

    def start(self):
        self.running = True
        while self.running:
            choice = input(
                "What would you like? (espresso/latte/cappuccino): ").strip()
            if choice == "off":
                self.running = False
            elif choice == "report":
                print(self.get_report())
            elif choice == "restock":
                self.restock(300, 200, 30)
            elif choice in self.menu.get_items():
                self.make(choice)
            else:
                print("We don't serve this type of coffee.")
