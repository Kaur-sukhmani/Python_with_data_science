# DECORATOR:
"""
RULE :
1. create a func which take func as input
2. create an inner func , which should have same signature of the target function
3. execute the passed func from inner function
4. return inner func from outer func
5. to decorate any function use @function
"""


def upgrade_to_meal(func):
    def inner(amount, taxes, meal_plan):
        if meal_plan == 1:
            print("Upgrading to medium meal...")
            print("+Added Coke")
            print("+Added fries")
            amount += 100
            taxes = 0.18
        elif meal_plan == 2:
            print("Upgrading to Large meal...")
            print("+Added Large Coke")
            print("+Added Large fries")
            print("+Added Ice Cream")
            amount += 200
            taxes = 0.20
        else:
            print("Thank you for your purchase")

        return func(amount, taxes, meal_plan)

    return inner


@upgrade_to_meal
def buy_burger(amount, taxes, meal_plan=0):
    return amount + (amount * taxes)


# result = compute_taxes(pay)
# result()

amount_to_pay = buy_burger(100, 0.5, 2)
print("McDonald's final charge ", amount_to_pay)


