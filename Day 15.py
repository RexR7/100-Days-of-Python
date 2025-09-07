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
}
coffee_machine_on = True
while coffee_machine_on:
    ques = str(input('''What would you like? espresso, latte or cappuccino:
Type 'off' to turn off coffee machine.
Type 'report' to get resource values. ''')).lower().strip()
    if ques == "off":
        coffee_machine_on = False
    elif ques == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")
    elif ques == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            quarters = int(input('''Please insert coins.
How many quarters? '''))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            money_inserted = 0
            money_inserted += quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
            if money_inserted > 1.5:
                print(f"Here's your change: ${money_inserted - 1.5}")
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            elif money_inserted == 1.5:
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                print("Perfect amount. Here's your espresso 🍵.")
            else:
                print("Sorry, that's not enough money. Money refunded!")
        elif resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print(f"Sorry, there is not enough water.")
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print(f"Sorry, there is not enough coffee.")
    elif ques == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            quarters = int(input('''Please insert coins.
How many quarters? '''))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            money_inserted = 0
            money_inserted += quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            if money_inserted > 2.5:
                print(f"Here's your change: ${money_inserted - 2.5}")
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            elif money_inserted == 2.5:
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                print("Perfect amount. Here's your latte 🍵.")
            else:
                print("Sorry, that's not enough money. Money refunded!")
        elif resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print(f"Sorry, there is not enough water.")
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print(f"Sorry, there is not enough milk.")
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print(f"Sorry, there is not enough coffee.")
    elif ques == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            quarters = int(input('''Please insert coins.
How many quarters? '''))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            money_inserted = 0
            money_inserted += quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            if money_inserted > 3.0:
                print(f"Here's your change: ${money_inserted - 3.0}")
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            elif money_inserted == 3.0:
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                print("Perfect amount. Here's your cappuccino 🍵.")
            else:
                print("Sorry, that's not enough money. Money refunded!")
        elif resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print(f"Sorry, there is not enough water.")
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print(f"Sorry, there is not enough milk.")
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print(f"Sorry, there is not enough coffee.")