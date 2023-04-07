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

def run_coffee_machine(resource_status, profit_status, response):
    ingredients = MENU.get(response).get("ingredients").keys()
    coffee_requires = MENU.get(response).get("ingredients")
    for ingredient in ingredients:
        if not (resource_status.get(f"{ingredient}") >= coffee_requires.get(f"{ingredient}", 0)):
            print(f"sorry there is not enough {ingredient}")

def print_report(resource_status, profit_status):
    report = f"""
Water: {resource_status.get("water")}ml
Milk: {resource_status.get("milk")}ml
Coffee: {resource_status.get("coffee")}g
Money: ${profit_status}
"""
    print(report)


            return resource_status, profit_status
    print("Please insert coins")
    cost_coffee = MENU.get(response).get("cost")
    money_inserted = count_money()
    if money_inserted >= cost_coffee:
        resource_status = make_coffee(response, resource_status)
        change = round((money_inserted - cost_coffee), 2)
        profit_status += cost_coffee
        give_coffee = f"""
Here is ${change} in change.
Here is your {response} ☕. Enjoy!            
        """
        print(give_coffee)
        return resource_status, profit_status
    else:
        print("Sorry that's not enough money. Money refunded.")
        return resource_status, profit_status


def count_money():
    quarters = int(input("how many quarters?:")) * 0.25
    dimes = int(input("how many dimes?:")) * 0.1
    nickels = int(input("How many nickels?:")) * 0.05
    pennies = int(input("How many pennies?:")) * 0.01
    total = round((quarters + dimes + nickels + pennies), 2)
    return total


def make_coffee(coffee_type, resource_status):
    ingredients = MENU.get(coffee_type).get("ingredients")
    items_used = ingredients.keys()
    for item in items_used:
        resource_status[item] -= ingredients.get(item)
    return resource_status


def coffee_machine(resources, profit, switch):
    while switch != 'off':
        response = input("What would you like? (espresso/latte/cappuccino):")
        if response in ["espresso", "latte", "cappuccino"]:
            resources, profit = run_coffee_machine(resources, profit, response)
        elif response == 'report':
            print_report(resources, profit)
        elif response == 'off':
            switch = 'off'
        else:
            print("Sorry. I did not understand that")


if __name__ == "__main__":
    init_profit = 0
    init_resources = {
        "water": 500,
        "milk": 500,
        "coffee": 100,
    }

    coffee_machine(init_resources, init_profit, switch='on')
