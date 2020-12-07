from prettytable import PrettyTable


table = PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.add_row(["Bulbasaur", "Poison"])
table.add_row(["Chramander", "Fire"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Caterpie", "Bug"])
table.add_row(["Pikachu", "Electric"])
table.align = "l"
print(table)
