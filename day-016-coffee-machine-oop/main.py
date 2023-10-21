from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()


is_on = True
while is_on:
    option = input(f"What would you like? ({menu.get_items()})? ")

    if option == "off":
        is_on = False
    elif option == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        order = menu.find_drink(option)
        if coffeeMaker.is_resource_sufficient(order) and moneyMachine.make_payment(order.cost):
            coffeeMaker.make_coffee(order)
