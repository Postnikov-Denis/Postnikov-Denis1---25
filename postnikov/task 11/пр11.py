def zad1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"В ресторане '{self.restaurant_name}'  {self.cuisine_type} кухня.")
        def open_restaurant(self):
            print(f"Ресторан '{self.restaurant_name}' открыт.")
    newRestaurant = Restaurant("Guisto", "итальянская")
    print(f"Название ресторана: {newRestaurant.restaurant_name}")
    print(f"Тип кухни: {newRestaurant.cuisine_type}")
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def zad2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"В ресторане '{self.restaurant_name}' {self.cuisine_type} кухня.")

        def open_restaurant(self):
            print(f"Ресторан '{self.restaurant_name}' открыт.")
    restaurant1 = Restaurant("Table by Bruno Verjus", "французская")
    restaurant2 = Restaurant("Lido 84", "итальянская")
    restaurant3 = Restaurant("Sorn", "азиатская")
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
def zad3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rat):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rat = rat
        def describe_restaurant(self):
            print(f"В ресторане  '{self.restaurant_name}' {self.cuisine_type} кухня. Рейтинг: {self.rat}")
        def open_restaurant(self):
            print(f"Ресторан '{self.restaurant_name}' открыт.")
        def update_rating(self, new_rat):
            self.rat = new_rat
            print(f"Рейтинг ресторана '{self.restaurant_name}' обновлен: {self.rat}")

    restaurant1 = Restaurant("Table by Bruno Verjus", "французская", 4.5)
    restaurant2 = Restaurant("Lido 84", "итальянская", 4.8)
    restaurant3 = Restaurant("Sorn", "азиатская", 4.9)
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

    restaurant1.update_rating(4.99)
    restaurant1.describe_restaurant()
zad3()
