class Coffee:

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
