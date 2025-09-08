MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print("\nCurrent Resources:")
    for key, value in resources.items():
        print(f"{key}: {value}")


def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_payment(drink):
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    money_inserted = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    cost = MENU[drink]["cost"]

    if money_inserted < cost:
        print("Sorry, that's not enough money. Money refunded!")
        return False
    elif money_inserted > cost:
        print(f"Here is ${round(money_inserted - cost, 2)} in change.")

    return True


def make_coffee(drink):
    for item, amount in MENU[drink]["ingredients"].items():
        resources[item] -= amount
    print(f"Here is your {drink} ☕. Enjoy!")

coffee_machine_on = True

while coffee_machine_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower().strip()

    if choice == "off":
        coffee_machine_on = False
    elif choice == "report":
        report()
    elif choice in MENU:
        if check_resources(choice):
            if process_payment(choice):
                make_coffee(choice)
    else:
        print("Invalid choice. Please try again.")
