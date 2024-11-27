import json

x = '{"name": "andres", "lastname" : "pacheco cuadro", "age" : "20"}'

y = json.loads(x)

print(y)

dictionanry = {
    "name": "andres",
    "lastname": "pacheco cuadro",
    "age": "20",
    "country" : "Colombia"
}

toJson = json.dumps(dictionanry)

print(toJson)