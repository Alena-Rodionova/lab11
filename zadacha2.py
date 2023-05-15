class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана {self.restaurant_name} Кухня: {self.cuisine_type}.")

    def open_restaurant(self):
        print("Ресторан сейчас открыт")


     # Создаем три экземпляра класса Restaurant
restaurant1 = Restaurant("О море", "Итальянская")
restaurant2 = Restaurant("Драконий берег", "Фастфуд")
restaurant3 = Restaurant("Гейша", "Японская")

    # Вызываем метод describe_restaurant() для каждого экземпляра
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


