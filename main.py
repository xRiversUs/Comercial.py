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




#Marcelo Rios

produtos = [
    ["Arroz", 25.90, 10],
    ["Feijão", 8.50, 15],
    ["Macarrão", 5.20, 20],
    ["Açúcar", 10.55, 30],
    ["Café", 20.90, 40],
    ["Óleo", 10.99, 30],
    ["Farinha", 15.65, 25],
    ["Sal", 10.50, 40]
]

matriz_estoque = [produtos[i:i + 4] for i in range(0, len(produtos), 4)]



for produto in produtos:
    print(f"Nome: {produto[0]}")
    print(f"Preço: {produto[1]:.2f}")
    print(f"Quantidade: {produto[2]}")
    print(" -------------- ")

#pedro henrike da costa
def iniciar():
    print("Sistema StockSync iniciado!")


def mostrar_produtos():
    print("\n--- Produtos em Estoque ---")
    for produto in produtos:
        print(f"{produto[0]} - R$ {produto[1]:.2f} - Quantidade: {produto[2]}")


def converter_custo_para_float(custo):
    try:
        if isinstance(custo, str):
            custo_limpo = custo.strip().replace("R$", "").replace(" ", "")
            if "," in custo_limpo:
                custo_limpo = custo_limpo.replace(".", "").replace(",", ".")
            custo = float(custo_limpo)
        else:
            custo = float(custo)
    except (TypeError, ValueError):
        print(f"Erro: custo inválido '{custo}'. O valor não pôde ser convertido.")
        return None

    return custo


def converter_custos_da_matriz():
    for prateleira in matriz_estoque:
        for produto in prateleira:
            produto[1] = converter_custo_para_float(produto[1])


def calcular_custo_total():
    custo_total = 0.0

    for prateleira in matriz_estoque:
        for produto in prateleira:
            custo = converter_custo_para_float(produto[1])
            if custo is not None:
                produto[1] = custo
                custo_total += custo

    return custo_total


def formatar_moeda_brl(valor):
    valor_formatado = f"{valor:.2f}"
    inteiro, decimal = valor_formatado.rsplit(".", 1)
    inteiro = f"{int(inteiro):,}".replace(",", ".")
    return f"R$ {inteiro},{decimal}"


def mostrar_painel_consolidado():
    custo_total = calcular_custo_total()

    print("\n" + "=" * 42)
    print("        PAINEL CONSOLIDADO STOCKSYNC")
    print("=" * 42)
    print(f"EMPRESA: {Empresa['nome']}")
    print(f"TIPO: {Empresa['tipo']}")
    print(f"RAMO: {Empresa['ramo']}")
    print(f"CIDADE: {Empresa['cidade']}")
    print(f"ANO DE FUNDAÇÃO: {Empresa['ano-fundacao']}")
    print("-" * 42)
    print("PRODUTOS E CUSTOS:")

    contador = 1
    for prateleira in matriz_estoque:
        for produto in prateleira:
            custo = converter_custo_para_float(produto[1])
            if custo is not None:
                print(f"Produto {contador}: {produto[0]} - {formatar_moeda_brl(custo)}")
                contador += 1

    print("-" * 42)
    print(f"# CUSTO TOTAL: {formatar_moeda_brl(custo_total)}")
    print("=" * 42)


def mostrar_matriz_estoque():
    print("\n--- Matriz 2D do Estoque (Prateleiras) ---")
    for indice_prateleira, prateleira in enumerate(matriz_estoque, start=1):
        posicoes = [
            f"Posição {indice_posicao}: {produto[0]} ({produto[2]} un.)"
            for indice_posicao, produto in enumerate(prateleira, start=1)
        ]
        print(f"Prateleira {indice_prateleira} | " + " | ".join(posicoes))


def verificar():
    print("Verificação de estoque iniciada!")


def encerrar():
    print("Sistema StockSync encerrado!")


def menu():
    print("\n===== STOCKSYNC =====")
    print("1 - Iniciar sistema")
    print("2 - Mostrar produtos")
    print("3 - Verificar estoque")
    print("4 - Encerrar o sistema")
    print("5 - Mostrar estoque")
    print("6 - Mostrar Painel consolidado")

    opcao = input("Escolha uma opção: ").strip()

    if not opcao:
        print("Entrada vazia! Digite uma opção de 1 a 6.")
    elif opcao == "1":
        iniciar()
    elif opcao == "2":
        mostrar_produtos()
    elif opcao == "3":
        verificar()
    elif opcao == "4":
        encerrar()
        return False
    elif opcao == "5":
        mostrar_matriz_estoque()
    elif opcao == "6":
        mostrar_painel_consolidado()
    else:
        print("Opção inválida! Escolha de 1 a 6.")

    return True


def main():
    converter_custos_da_matriz()
    while True:
        if not menu():
            break


if __name__ == "__main__":
    main()

#breno nadal rossi
