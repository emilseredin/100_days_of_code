class CashRegistry:

    def __init__(self):
        self.money = 0
        self.coins = {
            "quarter": 0.25,
            "dime": 0.1,
            "nickle": 0.05,
            "penny": 0.01
        }

    def process_coins(self, required):
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
                value_inserted += self.coins[coin_type] * coin_amount
                value_left = required - value_inserted
                if value_left >= 0:
                    print("${} more to insert.".format(value_left))
        return value_inserted

    def parse_transaction(self, cost):
        value_inserted = self.process_coins(cost)
        if value_inserted == cost:
            self.money = value_inserted
            return True, None
        elif value_inserted > cost:
            self.money += cost
            change = value_inserted - cost
            return True, change
        else:
            return False, None

    def get_report(self):
        return {
            "Money": self.money
        }
