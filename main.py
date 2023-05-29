def q1():
    class Rest:
        def __init__(self, rest_name, cuisine_type):
            self.rest_name = rest_name
            self.cuisine_type = cuisine_type

        def describe_rest(self):
            print(f"Название Ресторана: {self.rest_name},  кухня:  {self.cuisine_type} итальянская.")

        def open_rest(self):
            print("Ресторан сейчас открыт.")


    newRest = Rest("Итальянский сапожок"," ")
    print(newRest.rest_name)
    print(newRest.cuisine_type)

    newRest.describe_rest()
    newRest.open_rest()

def q2():

    class Rest:
        def __init__(self, rest_name, cuisine_type):
            self.rest_name = rest_name
            self.cuisine_type = cuisine_type

        def describe_rest(self):
            print(f"Название ресторана: {self.rest_name}, Кухня: {self.cuisine_type}.")
        def open_rest(self):
            print("Ресторан сейчас открыт")

    rest1 = Rest("Итальянский сапожок", "Итальянская")
    rest2 = Rest("За углом", "Домашняя")
    rest3 = Rest("Красное солнце", "Японская")

    rest1.describe_rest()
    rest1.open_rest()

    rest2.describe_rest()
    rest2.open_rest()

    rest3.describe_rest()
    rest3.open_rest()

def q3():
    class Rest:
        def __init__(self, rest_name, cuisine_type, initial_rating):
            self.rest_name = rest_name
            self.cuisine_type = cuisine_type
            self.rating = initial_rating

        def describe_rest(self):
            print(f"Название ресторана {self.rest_name}кухня: {self.cuisine_type}  итальянская .")

        def open_rest(self):
            print("Ресторан сейчас открыт.")

        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана: <{self.rest_name}> Был обновлен до  {self.rating}")

    rest = Rest("Итальянский сапожок", "Итальянская", 5)

    print(f"Первоначалальный рейтинг ресторана: <{rest.rest_name}>  {rest.rating}" )

    rest.update_rating(4.7)
    print(f"Обновленный рейтинг:  <{rest.rest_name}> : {rest.rating}")


q1()