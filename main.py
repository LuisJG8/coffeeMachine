from cMachineData import MENU, resources

PENNY_VALUE = 0.01
DIME_VALUE = 0.10
NICKEL_VALUE = 0.05
QUARTER_VALUE = 0.25
CHANGE = 0.00

coffee = input("What would you like? (espresso/latte/capuccino)")
print("Please insert your coins")
quarters = input("How many quarters")
dimes = input("How many dimes")
nickles = input("How many nickles")
pennies = input("How many pennies")

def machine(type_of_c):
    if type_of_c == 'espresso':
       dif = resources["water"] - MENU["espresso"]["ingredients"]["water"]
       print(dif)



machine(type_of_c=coffee)
        # m_1=quarters, m_2=dimes, m_3=nickles, m_4=pennies)