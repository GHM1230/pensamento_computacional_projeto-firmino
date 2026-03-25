'''

CRUD

sistema de ajuda para açaíteria

'''

print("bem vindo ao sistema de ajuda da açaíteria! como posso ajudar?")
print("1 - Cardápio")
print("2 - Horário de funcionamento")
print("3 - Localização")
print("4 - Contato")
print("5 - Sair")

opcao = input("Digite o número da opção desejada: ")

if opcao == "1":
    print("\nNosso cardápio inclui:")
    print("- Açaí na tigela")
    print("- Açaí com frutas")
    print("- Açaí com leite em pó")
    print("- Açaí com chocolate")
    print("- Açaí com coco")
    print("- Açaí com amendoim")
    print("- Açaí com morango")
    print("- Açaí com granola")
    print("- Açaí com leite de amêndoas")
    print("- Açaí com leite de coco")
    print("- Açaí com leite de soja")
    print("- Açaí com leite")
    print("- Açaí com leite condensado\n")

elif opcao == "2":
    print("\nNosso horário de funcionamento é:")
    print("Segunda a sexta: 10h às 22h")
    print("Sábado: 10h às 23h")
    print("Domingo: 12h às 20h\n")

elif opcao == "3":
    print("\nNossa localização é:")
    print("Av. seila-aonde, 67 - São Paulo/SP")
    print("Rua sem-nome, 99 - São Paulo/SP")
    print("Rua escura, 24 - São Paulo/SP\n")

elif opcao == "4":
    print("\nNosso contato é:")
    print("Telefone: (99) 99999-9999")
    print("Email: contato@acaíteria.com\n")


elif opcao == "5":
    print("\nObrigado por usar nosso sistema de ajuda! Até mais!\n")

else:
    print("\nOpção inválida. Por favor, escolha uma opção válida.\n")