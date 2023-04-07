from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_cafe = CoffeeMaker()
coffee_menu = Menu()
money_handler = MoneyMachine()
switch = 'on'
while switch != 'off':
    response = input(f"what would you like? ({coffee_menu.get_items()}): ")
    if response == 'off':
        switch = 'off'
    elif response == 'report':
        my_cafe.report()
        money_handler.report()
    elif coffee := coffee_menu.find_drink(response):
        if my_cafe.is_resource_sufficient(coffee):
            if money_handler.make_payment(coffee.cost):
                my_cafe.make_coffee(coffee)



