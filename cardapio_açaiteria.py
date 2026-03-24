pedido = []
total = 0

while True:
    print("\n--- CARDÁPIO DA AÇAITÉRIA ---")
    print("1 - Açaí pequeno - R$15")
    print("2 - Açaí médio - R$19")
    print("3 - Açaí grande - R$25")
    print("4 - Suco - R$7")
    print("5 - Finalizar pedido")
    print("0 - Sair")

    opcao = input("Escolha um item: ")

    if opcao in ["1", "2", "3", "4"]:
        try:
            quantidade = int(input("Quantos você quer? "))

            if quantidade <= 0:
                print("Digite um número válido!")
                continue

            if opcao == "1":
                pedido.append(f"{quantidade}x Açaí pequeno")
                total += 15 * quantidade

            elif opcao == "2":
                pedido.append(f"{quantidade}x Açaí médio")
                total += 19 * quantidade

            elif opcao == "3":
                pedido.append(f"{quantidade}x Açaí grande")
                total += 25 * quantidade

            elif opcao == "4":
                pedido.append(f"{quantidade}x Suco")
                total += 7 * quantidade

            print("✅ Adicionado ao pedido!")

        except ValueError:
            print("Digite apenas números!")

    elif opcao == "5":
        print("\n--- RESUMO DO PEDIDO ---")
        
        if not pedido:
            print("Você não pediu nada.")
        else:
            for item in pedido:
                print("-", item)

            print(f"\nTotal: R${total:.2f}")

        print("\nPedido finalizado. Obrigado pela preferência!")
        break

    elif opcao == "0":
        print("\nSaindo sem finalizar pedido.")
        print("Volte sempre!")
        break

    else:
        print("Opção inválida. Tente novamente.")
    break