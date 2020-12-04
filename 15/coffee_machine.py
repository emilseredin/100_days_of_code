from menu import Menu
from cash_registry import CashRegistry
from coffee_maker import CoffeeMaker


class CoffeeMachine:

    def __init__(self):
        self.coffee_maker = CoffeeMaker(water=300, milk=200, coffee=100)
        self.cash_registry = CashRegistry()
        self.menu = Menu()
        self.running = False

    def get_report(self):
        report = self.coffee_maker.get_report()
        report.update(self.cash_registry.get_report())
        message = ""
        for element, quantity in report.items():
            measure = "ml"
            if element == "Coffee":
                measure = "g"
            if element == "Money":
                measure = "$"
                message += "{}: {}{}".format(element, measure, quantity)
            else:
                message += "{}: {}{}\n".format(element, quantity, measure)
        return message

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
                self.coffee_maker.restock(300, 200, 30)
            elif choice in self.menu.get_items():
                price = self.menu.get_price(choice)
                print("{} costs ${}".format(choice.capitalize(), price))
                success, change = self.cash_registry.parse_transaction(
                    cost=price)
                if success:
                    ingredients = self.menu.get_ingredients(choice)
                    message = self.coffee_maker.make(choice, ingredients)
                else:
                    message = "Sorry, that's not enough money. Money refunded."
                if change:
                    message += "\nHere is ${} in change.".format(change)
                print(message)
            else:
                print("We don't serve this type of coffee.")
