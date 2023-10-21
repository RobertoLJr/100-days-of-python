COMMANDS = ["off", "report", "refill", "espresso", "latte", "cappuccino"]

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 50
}


def report():
    print(f"Water:  {resources['water']} mL")
    print(f"Milk:   {resources['milk']} mL")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money:  $ {resources['money']:.2f}")


def is_resource_available(order_ingredients):
    """Return True if available resources in the machine for a particular drink, otherwise return False."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """Return True if payment equals to or higher than drink cost, otherwise return False"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > resources["money"]:
            print("Sorry, there's not enough change for this amount. Money refunded.")
            return False
        if money_received > drink_cost:
            print(f"Here is $ {change} in change.")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_drink(drink_name, order_ingredients):
    """Deduct the required ingredients from resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


def process_coins():
    """Return total value from four types of coins inserted."""
    print("Please, insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def refill():
    """Ask for amounts for every resource to be added to the machine."""
    resources["water"] += int(input("How much water would you like to add (mL)? "))
    resources["milk"] += int(input("How much milk would you like to add (mL)? "))
    resources["coffee"] += int(input("How much coffee would you like to add (g)? "))
    resources["money"] += float(input("How much money would you like to add ($)? "))


is_on = True
while is_on:
    option = input("What would you like (espresso/latte/cappuccino)? ")

    if option == "off":
        is_on = False
    elif option == "report":
        report()
    elif option == "refill":
        refill()
    elif option in COMMANDS:
        drink = MENU[option]
        if is_resource_available(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_drink(option, drink["ingredients"])
    else:
        print("Unknown command. Please, try again.")
