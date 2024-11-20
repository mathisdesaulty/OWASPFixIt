import jsonpickle

# Exemple d'objet Python
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

# Créer une instance de la classe
person = Person("Alice", 30, "Wonderland")

# Sérialiser l'objet en JSON
json_data = jsonpickle.encode(person)

# Écrire le JSON dans un fichier
with open('example.json', 'w') as json_file:
    json_file.write(json_data)
