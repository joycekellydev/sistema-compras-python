def cadastrar_produtos(produtos):
    while True:
        print("\n--- Cadastro de Produto ---")

        nome = input("Nome do produto: ").strip()
        while not nome:
            print("Nome não pode ser vazio.")
            nome = input("Nome do produto: ").strip()

        while True:
            try:
                preco = float(input("Preço unitário: "))
                if preco <= 0:
                    print("O preço deve ser maior que zero.")
                else:
                    break
            except ValueError:
                print("Valor inválido!")

        while True:
            try:
                quantidade = int(input("Quantidade: "))
                if quantidade <= 0:
                    print("Quantidade deve ser maior que zero.")
                else:
                    break
            except ValueError:
                print("Valor inválido!")

        subtotal = preco * quantidade

        produtos.append({
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "subtotal": subtotal
        })

        print("Produto cadastrado com sucesso!")

        continuar = input("Deseja adicionar outro produto? (s/n): ").lower()
        if continuar != "s":
            break


def calcular_total(produtos):
    return sum(p["subtotal"] for p in produtos)


def escolher_pagamento(total):
    print("\n1 - À vista")
    print("2 - Cartão")

    while True:
        opcao = input("Escolha: ")
        if opcao in ("1", "2"):
            break
        print("Opção inválida!")

    desconto = 0

    if opcao == "1":
        if total > 200:
            desconto = total * 0.15
        elif total >= 100:
            desconto = total * 0.10
        print("Desconto aplicado!")
    else:
        print("Sem desconto.")

    return desconto


def mostrar_relatorio(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    total = calcular_total(produtos)

    print("\n======= RELATÓRIO =======")
    for p in produtos:
        print(f"{p['nome']} | Qtd: {p['quantidade']} | R$ {p['subtotal']:.2f}")

    print(f"\nTotal: R$ {total:.2f}")


def finalizar_compra(produtos):
    if not produtos:
        print("Cadastre produtos antes de finalizar.")
        return

    total = calcular_total(produtos)
    desconto = escolher_pagamento(total)
    total_final = total - desconto

    print("\n======= FINALIZAÇÃO =======")
    print(f"Total: R$ {total:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total final: R$ {total_final:.2f}")


def menu():
    produtos = []

    while True:
        print("\n====== MENU ======")
        print("1 - Cadastrar produtos")
        print("2 - Ver relatório")
        print("3 - Finalizar compra")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produtos(produtos)

        elif opcao == "2":
            mostrar_relatorio(produtos)

        elif opcao == "3":
            finalizar_compra(produtos)

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()