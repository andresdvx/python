
def return_value(key):
    car = {
        "brand": "ferrari",
        "model": "Ferrari f8 spider",
        "year": 2002,
    }

    if key in car:
        return car[key]
    else:
        return "this key does not exist"

print(return_value("checo"))


def filtrar_diccionario(dictionary, umbral_value):
    new_dictionary = {}
    for key, value in dictionary.items():

        if value > umbral_value:
            new_dictionary[key] = value

    return new_dictionary


datos = {"manzanas": 5, "naranjas": 3, "bananas": 7}
umbral = 4

print(filtrar_diccionario(datos, umbral))


def valores_unicos(lista):
    new_list = []
    existing = set()

    for item in lista:

        if item not in existing:
            new_list.append(item)
            existing.add(item)

    return new_list

numeros = [1, 2, 3, 2, 1, 4]

print(valores_unicos(numeros))

def list_to_dictionary(list1, list2):
    dictionary = {}
    if len(list1) != len(list2):
        return "list doesn't match"

    # opcion con funcion zip

    # dictionary = dict(zip(list1, list2))

    for index in range(len(list1)):
        dictionary[list1[index]] = list2[index]

    return dictionary


claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 25, "Madrid"]

print(list_to_dictionary(claves, valores))
