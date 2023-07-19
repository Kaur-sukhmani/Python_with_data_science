# Redefine the function
def compute_taxes(amount=100, tax=18):
    amount_to_pay = amount + (amount * tax / 100)
    return amount_to_pay


old_compute_taxes = compute_taxes
print("Compute taxes:", compute_taxes)


def compute_taxes(amount=100, tax=12, extra=0.10):
    amount_to_pay = amount + (amount * tax / 100) + extra * amount
    return amount_to_pay


print("Compute taxes now is :", compute_taxes)

print(compute_taxes())


class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __init__(self, name="noodles", price=299, ratings=4.0):
        self.name = name
        self.price = price
        self.ratings = ratings


dish1 = Dish()
print("data in dish1:", vars(dish1))

print("Old compute taxes:", old_compute_taxes())
