from data import MENU
from data import resources

# TODO: 1. Print a todo (haha)

money = {"quarter": 0.25,
         "dime": 0.1,
         "nickle": 0.05,
         "pennie": 0.01}
profit = 0


def resources_check(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        if resources[ingredient] < MENU[coffee]["ingredients"][ingredient]:
            print(f"Sorry, it's not enough {ingredient}")
            program()
    for ingredient in MENU[coffee]["ingredients"]:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]


def program():
    global profit
    user_choice = input("Choose coffee you want: Espresso, Latte, Cappuccino: ").lower()

    if user_choice == "off":
        return
    elif user_choice == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee:{resources["coffee"]}ml\nMoney: {profit}$")
        program()
    elif user_choice not in ["espresso", "latte", "cappuccino"]:
        print("You didn't choose any of our positions. Please choose from the menu.")
        program()

    resources_check(user_choice)
    print(f"\nThe price is: {MENU[user_choice]["cost"]}$")
    print("Please insert the coins.")
    amount_quarters = int(input("How many quarters? "))
    amount_dimes = int(input("How many dimes? "))
    amount_nickles = int(input("How many nickles? "))
    amount_pennies = int(input("How many pennies? "))

    money_from_a_client = amount_quarters * 0.25 + amount_dimes * 0.1 + amount_nickles * 0.05 + amount_pennies * 0.01

    if money_from_a_client < MENU[user_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        program()

    change = money_from_a_client - MENU[user_choice]["cost"]
    profit += MENU[user_choice]["cost"]

    print(f"\nHere is {round(change, 2)}$ in change")
    print(f"Here is your {user_choice} ☕️. Enjoy!\n")

    program()


program()
