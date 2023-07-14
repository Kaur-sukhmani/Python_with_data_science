#Most appropriate way to write in main function


from sess7 import Restaurant, Menu, Dish

def main():
    restaurant = Restaurant(
        name="Maharaja",
        address="Ludhiana, Model Town ",
        phone="+91 939439334",
        rating=4.5,
        menu=Menu(
            title="Indian Delight",
            num_of_dishes=5,
            dishes=[
                Dish(name="Dal Makhani", price=350, rating=4.5),
                Dish(name="Paneer Do Pyaza", price=450, rating=5.0),
                Dish(name="Noodles", price=250, rating=3.8),
                Dish(name="Burger", price=100, rating=4.1),
                Dish(name="Fries", price=90, rating=4.8)
            ])

    )
    restaurant.show()


if __name__ == "__main__":
    main()