#PROGRAM STILL IN PROGRESS
#PROGRAM IS VERBOSE AND NOT OPTIMAL

from cMachineData import MENU, resources
from logo import art

PENNY_VALUE = 0.01
DIME_VALUE = 0.10
NICKEL_VALUE = 0.05
QUARTER_VALUE = 0.25
change = 0.00

print(art)

flag = True

while flag:
    coffee = input("What would you like? (espresso/latte/capuccino): ").lower()
    print("Please insert your coins")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    total_money = (QUARTER_VALUE * quarters) + (DIME_VALUE * dimes) + (NICKEL_VALUE * nickles) + (PENNY_VALUE * pennies)
    total_money = float(total_money)
    def resource_handling_machine(type_of_c):

        if type_of_c == 'espresso' and MENU["espresso"]["ingredients"]["water"] >= 50 and MENU["espresso"]["ingredients"]["coffee"] >= 18:
           minus_w_e = resources["water"] - MENU["espresso"]["ingredients"]["water"]
           print(minus_w_e)
           minus_c_e = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
           print(minus_c_e)

           MENU["espresso"]["ingredients"]["water"] = minus_w_e
           MENU["espresso"]["ingredients"]["coffee"] = minus_c_e
           return minus_c_e, minus_w_e
        else:
            print("Not enough water or coffee")
        if type_of_c == 'latte' and MENU["latte"]["ingredients"]["water"] >= 200 and MENU["latte"]["ingredients"]["milk"] >= 150 and MENU["latte"]["ingredients"]["coffee"] >= 24:
            minus_w_l = resources["water"] - MENU["latte"]["ingredients"]["water"]
            minus_m_l = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            minus_c_l = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]

            MENU["latte"]["ingredients"]["coffee"] = minus_c_l
            MENU["latte"]["ingredients"]["milk"] = minus_m_l
            MENU["latte"]["ingredients"]["coffee"] = minus_w_l
            return minus_c_l, minus_w_l, minus_m_l
        else:
            print("Not enough water, milk or coffee")
        if type_of_c == 'cappuccino' and MENU["cappuccino"]["ingredients"]["water"] >= 250 and MENU["cappuccino"]["ingredients"]["milk"] >= 100 and MENU["cappuccino"]["ingredients"]["coffee"] >= 24:
            minus_w_c = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            minus_m_c = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            minus_c_c = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]

            MENU["cappuccino"]["ingredients"]["water"] = minus_w_c
            MENU["cappuccino"]["ingredients"]["milk"] = minus_m_c
            MENU["cappuccino"]["ingredients"]["water"] = minus_w_c
            return minus_c_c, minus_w_c, minus_m_c
        else:
            print("Not enough water, milk or coffee")
    def money_handling_machine(money, type_of_c):
        if type_of_c == "espresso" and money < MENU["espresso"]["cost"]:
            print("Not enough money. Money refunded")
        elif type_of_c == "espresso" and money > MENU["espresso"]["cost"]:
            old_change = money - MENU["espresso"]["cost"]
            change = round(old_change, 3)
            print(f"Here is your change{change}")
            return change
        elif type_of_c == 'latte' and money < MENU["latte"]["cost"]:
            print("Not enough money. Money refunded")
        elif type_of_c == 'latte' and money > MENU["latte"]["cost"]:
            old_change = money - MENU["latte"]["cost"]
            change = round(old_change, 3)
            print(f"Here is your change {change}")
            return change
        elif type_of_c == 'cappuccino' and money < MENU["cappuccino"]["cost"]:
            print("Not enough money. Money refunded")
        elif type_of_c == 'cappuccino' and money > MENU["cappuccino"]["cost"]:
            old_change = money - MENU["cappuccino"]["cost"]
            change = round(old_change, 3)
            print(f"Here is your change {change}")
            return change

    m_machine = money_handling_machine(total_money, coffee)

    resource_handling_machine(type_of_c=coffee)
    money_handling_machine(money=total_money, type_of_c=coffee)
