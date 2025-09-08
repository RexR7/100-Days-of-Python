from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
make_coffee = CoffeeMaker()
money_machine = MoneyMachine()

coffee_machine_on = True

while coffee_machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        coffee_machine_on = False
    elif choice == "report":
        make_coffee.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if make_coffee.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_made = make_coffee.make_coffee(drink)