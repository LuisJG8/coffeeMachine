from cMachineData import MENU, resources
from logo import art

PENNY_VALUE = 0.01
DIME_VALUE = 0.10
NICKEL_VALUE = 0.05
QUARTER_VALUE = 0.25
CHANGE = 0.00

print(art)

coffee = input("What would you like? (espresso/latte/capuccino): ")
print("Please insert your coins")
quarters = input("How many quarters?: ")
dimes = input("How many dimes?: ")
nickles = input("How many nickles?: ")
pennies = input("How many pennies?: ")

total_money = quarters + dimes + nickles + pennies

def resource_handling_machine(type_of_c):
    if type_of_c == 'espresso':
       minus_w_e = resources["water"] - MENU["espresso"]["ingredients"]["water"]
       print(minus_w_e)
       minus_c_e = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
       print(minus_c_e)
    elif type_of_c == 'latte':
        minus_w_l = resources["water"] - MENU["latte"]["ingredients"]["water"]
        print(minus_w_l)
        minus_m_l = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        print(minus_m_l)
        minus_c_l = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        print(minus_c_l)
    elif type_of_c == 'cappuccino':
        minus_w_c = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        print(minus_w_c)
        minus_m_c = resources["milk"] - MENU["espresso"]["ingredients"]["milk"]
        print(minus_m_c)
        minus_c_c = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        print(minus_c_c)


def money_handling_machine(money, type_of_c):
    if type_of_c == "espresso" and money < MENU["latte"]["cost"]:
        print("Not enough money. Money refunded")
    elif type_of_c == "espresso" and money > MENU["latte"]["cost"]:
        pass





resource_handling_machine(type_of_c=coffee)
money_handling_machine(money=total_money, type_of_c=coffee)
        # m_1=quarters, m_2=dimes, m_3=nickles, m_4=pennies)
