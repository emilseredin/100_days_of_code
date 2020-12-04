from helper import MENU, COINS


class CoffeeMachine:

    def __init__(self, water, milk, coffee):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = 0
        self.running = False

    def get_report(self):
        return "Water: {}ml\nMilk: {}ml\nCoffee: {}\nMoney: {}".format(self.water, self.milk, self.coffee, self.money)

    def restock(self, water, milk, coffee):
        self.water += water
        self.milk += milk
        self.coffee += coffee

    def process_coins(self, cost):
        insert_coins = True
        value_inserted = 0
        while insert_coins:
            coin_type = input(
                "Please choose the coin (penny/nickle/dime/quarter/stop): ").strip()
            if coin_type == "stop":
                insert_coins = False
            else:
                coin_amount = int(
                    input("How many coins of this kind will you insert? ").strip())
                value_inserted += COINS[coin_type] * coin_amount
                value_left = cost - value_inserted
                if value_left >= 0:
                    print("${} more to insert.".format(cost - value_inserted))
        if value_inserted == cost:
            self.money = value_inserted
            return True
        elif value_inserted > cost:
            self.money = cost
            change = value_inserted - cost
            print("Here is ${} in change.".format(change))
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

    def make(self, coffee):
        ingredients = MENU[coffee]["ingredients"]
        price = MENU[coffee]["cost"]
        if "water" in ingredients and self.water < ingredients["water"]:
            print("Sorry, there is not enough water.")
        elif "coffee" in ingredients and self.coffee < ingredients["coffee"]:
            print("Sorry, there is not enough coffee.")
        elif "milk" in ingredients and self.milk < ingredients["milk"]:
            print("Sorry, there is not enough milk.")
        else:
            print("{} costs ${}".format(coffee.capitalize(), price))
            if self.process_coins(cost=price):
                self.water = self.water - ingredients["water"]
                self.coffee = self.coffee - ingredients["coffee"]
                print("Here is your {}. Enjoy!".format(coffee))

    def start(self):
        self.running = True
        while self.running:
            answer = input(
                "What would you like? (espresso/latte/cappuccino): ").strip()
            if answer == "off":
                self.running = False
            elif answer == "report":
                print(self.get_report())
            elif answer == "restock":
                self.restock(300, 200, 30)
            elif answer in MENU:
                self.make(answer)
            else:
                print("We don't serve this type of coffee.")
