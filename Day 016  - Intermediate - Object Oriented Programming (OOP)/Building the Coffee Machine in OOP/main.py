# COFFEE MACHINE Project 

# Program Requiremwnts.
# 1. print report
# 2. check resources sufficient ?
# 3. process coins.
# 4. check transaction successful?
# 5. make coffee.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine 

money_machine = MoneyMachine()
Coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.grt_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        Coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = Coffee_maker.is_resources_sufficient(drink) 
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            Coffee_maker.make_coffee(drink)
