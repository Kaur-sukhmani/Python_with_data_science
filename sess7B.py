# AMAZON SHOPPING CART
"""
    1 Menu has many Options
    1 Option has Many Categories
    Many Categories has Many Products

"""
import self as self


# hamesha many waalis cheezain pehle likho
class Product:
    def __init__(self, name, brand, price, rating):
        self.name = name
        self.brand = brand
        self.price = price
        self.rating = rating

    def show(self):
        print("_____________________")
        print(self.name, "|", self.brand)
        print(self.price, "|", self.rating)
        print("_____________________")


class Category:
    def __init__(self, title, num_of_products, min_discount, products):
        self.title = title
        self.num_of_products = num_of_products
        self.min_discount = min_discount
        self.products = products

    def show(self):
        print("++++++++++++++++++++++")
        print(self.title, "|", self.num_of_products)
        print(self.min_discount)
        print("++++++++++++++++++++++")

    def show_products(self):
        for idx in range(len(self.products)):
            self.products[idx].show()


class Menu:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def show(self):
        print("======================")
        print(self.name)
        print("======================")

    def show_categories(self):
        for idx in range(len(self.categories)):
            self.categories[idx].show()


def main():
    smart_phone_products = [
        Product(name="iPhone13", brand="Apple", price=70000, rating=4.5),
        Product(name="Samsung Fold", brand="Samsung", price=90000, rating=4.6)
    ]

    mob_categories = [
        Category(title="Accessories", num_of_products=21, min_discount="40%", products=None),
        Category(title="Smart Phones", num_of_products=2, min_discount="30%", products=smart_phone_products),
        Category(title="Prime Day Launches", num_of_products=234, min_discount="50%", products=None),
    ]

    menu = [
        Menu(name="Sell", categories=None),
        Menu(name="Best Sellers", categories=None),
        Menu(name="Today's Deals", categories=None),
        Menu(name="Mobiles", categories=mob_categories),
        Menu(name="New Releases", categories=None)
    ]
    print("WELCOME TO AMAZON")
    for idx in range(len(menu)):
        menu[idx].show()

    print()
    menu_option = int(input("Choose the Menu (1-5): "))
    print("Menu Option Chosen:", menu_option)

    if menu_option == 4:
        menu[3].show_categories()

        category_choice = int(input("Select the Category(1-3): "))
        if category_choice == 2:
            mob_categories[1].show_products()


if __name__ == "__main__":
    main()
