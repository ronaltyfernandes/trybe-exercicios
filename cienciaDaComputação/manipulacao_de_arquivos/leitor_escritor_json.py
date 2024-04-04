import json  # json é um modulo que vem embutido, porém precisamos importá-lo

with open("comidas.json", mode="w") as comidas:
    adicionar_comidas = [
        "macarrão",
        "arroz",
        "pão",
        "chocolate",
        "nutela",
        "whey"
]
    # a json_to_write tranforma o valor da lista para json
    json_to_write = json.dumps(adicionar_comidas)
    comidas.write(json_to_write)

with open("comidas.json", mode="r") as arquivo:
    lista_comidas = json.load(arquivo)

# repetição usando a lista
for comida in lista_comidas:
    print(comida)

