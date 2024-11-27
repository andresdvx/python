car  = {
    "brand" : "ferrari",
    "model" : "Ferrari f8 spider",
    "year" : 2002,
}

# acceder a los valores del diccionario
print(car["model"])

print(car.get("brand"))

# actualizar un valor

car.update({"year": "2008"})
car.update({"model": "La Ferrari"})

print(car)

# agregar items

car["color"] = "red"

print(car)

# eliminar items

car.pop("year")

del car["color"]

print(car)

# recorrer diccionarios

for x in car: # recorre la clave
    print(x)

for x in car.values(): # recorre los valores
    print(x)

for x, y in car.items(): # recorre claves y valores
    print(x, y)