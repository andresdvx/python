
class Person:

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_country(self):
        return self.country

    def get_info(self):
        return {
            'name': self.name,
            'age': self.age,
            'country': self.country
        }

andres = Person('Andres', 20, 'COL')

print(andres.get_info())
