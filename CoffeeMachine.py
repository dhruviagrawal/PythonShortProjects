MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
}

profit = 0


def report():
    """generates a report that shows the current resources value"""
    water_amount = resources["water"]
    milk_amount = resources["milk"]
    coffee_amount = resources["coffee"]

    print(f"Water: {water_amount}ml \nMilk: {milk_amount}ml \nCoffee: {coffee_amount}g \nMoney: ${profit}")


def is_resources_sufficient(drink):
    """tells whether resources available are sufficient for a particular order"""
    water_needed = drink["ingredients"]["water"]
    milk_needed = drink["ingredients"]["milk"]
    coffee_needed = drink["ingredients"]["coffee"]
    if water_needed > resources["water"]:
        print("Sorry there is not enough water")
        return False
    elif milk_needed > resources["milk"]:
        print("Sorry there is not enough milk")
        return False
    elif coffee_needed > resources["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True


def transaction(drink, payment):
    """Checks and executes transaction"""
    cost_of_drink = drink["cost"]
    if cost_of_drink > payment:
        print("Sorry that's not enough money")
        print(f"{payment} Money refunded")
        return False
    else:
        global profit
        profit += cost_of_drink
        refund = round(payment - cost_of_drink, 2)
        print(f"Here is ${refund} dollars in change")
        return True


def make_drink(drink, prompt):
    water_needed = drink["ingredients"]["water"]
    milk_needed = drink["ingredients"]["milk"]
    coffee_needed = drink["ingredients"]["coffee"]
    resources["water"] -= water_needed
    resources["milk"] -= milk_needed
    resources["coffee"] -= coffee_needed
    print(f"Here is your {prompt}. Enjoy!!")


prompt = "on"
while prompt != "off":
    prompt = input("What would you like? (espresso/latte/cappuccino):").lower()
    if prompt == "report":
        report()
    elif prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        if is_resources_sufficient(MENU[prompt]):
            print("Insert coins to pay:-")
            quarter = int(input("Quarters: "))
            dimes = int(input("Dimes: "))
            nickles = int(input("Nickles: "))
            pennies = int(input("Pennies: "))
            money = (quarter * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
            money = round(money, 2)
            if transaction(MENU[prompt], money):
                make_drink(MENU[prompt], prompt)
    else:
        print("Coffee Machine closed for the day.")
