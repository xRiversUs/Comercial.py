Empresa = {
"nome": "StockSync",
"tipo": "Empresa Comercial",
"ramo": "Controle de Estoque",
"cidade": "São Paulo",
"ano-fundacao": "2026",
"telefone": "(11) 99686-8853",
"email": "contatostocksync@gmail.com.br"
}

produtos = {
    "Arroz", "Feijão", "Macarrão", "Açucar", "Café", "Óleo", "Farinha", "Sal"
}

funcionarios = {
    "Helena"
    "Geovana"
    "Sophia"
    "Rafael"
    "Joyce"
    "Lorena"
}

recursos = {
    "Sistema de Estoque"
    "Leitores de Código de Barra"
    "Computadores"
    "Veículos de entrega"
}

print(f"Nome: {Empresa['nome']}")
print(f"Tipo: {Empresa['tipo']}")
print(f"Ramo: {Empresa['ramo']}")
print(f"Cidade/Estado da empresa: {Empresa['cidade']}")
print(f"Ano de Fundação: {Empresa['ano-fundacao']}")
print(f"Telefone para contato: {Empresa['telefone']}")
print(f"E-mail da empresa: {Empresa['email']}")


#Marcelo Rios

produtos = [
    ["Arroz", 25.90, 10],
    ["Feijão", 8.50, 15],
    ["Macarrão", 5.20, 20],
    ["Açúcar", 10.55, 30],
    ["Café", 29.90, 40],
    ["Óleo", 10.99, 30],
    ["Farinha", 15.65, 25],
    ["Sal", 10.50, 40]
]

print(Empresa)

for produto in produtos:
    print(f"Nome: {produto[0]}")
    print(f"Preço: {produto[1]:.2f}")
    print(f"Quantidade: {produto[2]}")
    print(" -------------- ")