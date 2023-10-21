# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkSlateGrey")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable

# Baldur's Gate 3 characters
table = PrettyTable()
table.add_column("Name", ["Shadowheart", "Karlach", "Lae'zel"])
table.add_column("Class",
                 [
                     "Cleric",
                     "Barbarian",
                     "Fighter"
                 ])

table.align = 'l'
print(table)
