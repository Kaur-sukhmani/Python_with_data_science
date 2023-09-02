# DECORATOR:
"""
RULE :
1. create a func which take func as input
2. create an inner func , which should have same signature of the target function
3. execute the passed func from inner function
4. return inner func from outer func
5. to decorate any function use @function
"""


def compute_taxes(func):
    def inner(amount, taxes):
        if amount > 0 and amount <= 10000:
            taxes = 0.18  # update taxes
        elif amount > 10000:
            taxes = 0.25  # update taxes
        else:
            print("Invaid amount")

        return func(amount, taxes)

    return inner


@compute_taxes
def pay(amount, taxes):
    return amount + (amount * taxes)


# result = compute_taxes(pay)
# result()

amount_to_pay = pay(2000, 0.0)
print("amount_to_pay", amount_to_pay)


