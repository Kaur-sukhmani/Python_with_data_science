# STANDARDIZATION IN OOPS
"""
class Dish:
    pass


dish1 = Dish()
dish2 = Dish()
# dish1 and dish2 are reference vars
# they contain hashcode of objects :)
dish1.name = "noodles"
dish1.price = 303
dish1.ratings = 4.5

dish2.name = "Burger"
dish2.pricing = 100
dish2.rating = 4.3

print(vars(dish1))
print(vars(dish2))
print(vars(dish3))
"""

"""

# Object and attributes: Dishes, name, menu, price, ratings
class Dish:
    #Constructor
    def __init__(self):
        self.name = ""
        self.price = 0
        self.ratings = 4.3

dish1 = Dish()
dish2 = Dish()
print(vars(dish1))
print(vars(dish2))
"""
# O/p
"""
{'name': '', 'price': 0, 'ratings': 4.3}
{'name': '', 'price': 0, 'ratings': 4.3}
"""

# to cahnge the vales of diff objects in the constructor
class Dish:
    # CONSTRUCTOR
    def __init__(self, name="", price=0, ratings=4.0):
        self.name = name
        self.price = price
        self.ratings = ratings
    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("NAME:", self.name)
        print("PRICE:", self.price)
        print("RATINGS:", self.ratings)
        print("~~~~~~~~~~~~~~~~~~~~~~~~")


dish1 = Dish("Noodles", 300, 4.5)
dish2 = Dish("Burger", 100, 4.3)
dish3 = Dish(name="Fries")
dish1.show()
dish2.show()
dish3.show()
