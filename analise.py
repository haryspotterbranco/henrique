produtos = [
    {"nome": "Mochila", "preco": 120.50},
    {"nome": "Caderno", "preco": 25.00},
    {"nome": "Tênis", "preco": 180.00}
]

print("Produtos que custam mais de R$ 50,00:")

for produto in produtos:
    if produto["preco"] > 50.00:
        print(f"- {produto['nome']}")