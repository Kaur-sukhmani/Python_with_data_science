# # Assignment: Implement the same program Using OOPS from Session7 and Session7A
from sess7 import Menu, Dish

"""
    Zomato Cart
"""

class Cart:
    def __init__(self, item_ids=[], quantities=[], price=[], dishes=[]):
        self.item_ids = item_ids
        self.quantities = quantities
        self.dishes = dishes
        self.price = price

    def show(self):
        print(self.item_ids)
        for item in self.item_ids:
            print(self.dishes[item].name)
        print(self.quantities)

    def cart_total(self):
        return sum(self.price)


def apply_promo_code(amount, promo_code):
    if promo_code == "WELCOME50":
        if amount >= 159:
            print("Promo Code Applied Successfully...")

            discount = 0.50 * amount

            if discount >= 100:
                discount = 100

            amount_to_pay = amount - discount
            print("Please Pay: \u20b9", amount_to_pay)
        else:
            print("Amount is Lesser for Promo Code...")
            print("Please Pay: \u20b9", amount)

    elif promo_code == "ZOMPAYTM":
        if amount >= 299:
            print("Promo Code Applied Successfully...")

            discount = 0.20 * amount

            if discount >= 50:
                discount = 50

            amount_to_pay = amount - discount
            print("Please Pay: \u20b9", amount_to_pay)
            print("You will get a cashback of: \u20b9 25")
        else:
            print("Amount is Lesser for Promo Code...")
            print("Please Pay: \u20b9", amount)
    else:
        print("Promo Code Invalid")
        print("Please Pay: \u20b9", amount)


def main():
    dish1 = Dish(name="Dal Makhani", price=350, rating=4.5)
    dish2 = Dish(name="Paneer Do Pyaza", price=450, rating=5.0)
    dish3 = Dish(name="Noodles", price=250, rating=3.8)
    dish4 = Dish(name="Burger", price=100, rating=4.1)
    dish5 = Dish(name="Fries", price=90, rating=4.8)
    dish6 = Dish(name="Parantha", price=40, rating=4.2)
    dish7 = Dish(name="Cola", price=50, rating=4.7)

    # List of Objects :)
    dishes = [dish1, dish2, dish3, dish4, dish5, dish6, dish7]

    menu = Menu(title="Mix Delight", num_of_dishes=len(dishes), dishes=dishes)

    print("MENU:")
    menu.show()

    item_names = []
    quantities = []
    item_ids = []
    price = []

    while True:
        item_id = int(input("Enter Dish ID to add in Cart: "))
        quantity = int(input("Enter Dish Quantity: "))

        item_names.append(dishes[item_id].name)
        quantities.append(quantity)
        price.append(dishes[item_id].price * quantity)
        item_ids.append(item_id)

        print(price)

        choice = input("Do You wish to add more items? (yes/no)")
        if choice == "no":
            break

    cart1 = Cart(item_ids, quantities, price, dishes)
    amount = cart1.cart_total()

    print("CART:")
    cart1.show()
    print("TOTAL AMOUNT: \u20b9", amount)

    message = """
        Welcome to Zomato Coupons
        Today's Offers:

        WELCOME50
        Get 50% OFF up to ₹100
        Valid on total value of items worth ₹159 or more.


        ZOMPAYTM
        Get 20% OFF up to ₹50 and ₹25 Paytm cashback using Paytm
        Valid on total value of items worth ₹299 or more.

        RAINY
        Get 30% OFF up to ₹200.
        Valid on total value of items worth ₹499 or more.


    """

    print(message)
    promo_code = input("Enter Promo Code: ")
    apply_promo_code(amount, promo_code)


if __name__ == "__main__":
    main()

# Assignment: Implement the same program Using OOPS from Session7 and Session7A
