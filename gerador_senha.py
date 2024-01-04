import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*()-_{}|?^~0123456789'

def exibirMenu():
    print(">>>>>>>Gerador de senhas<<<<<<<<"
          "\n[1] - Gerar senha"
          "\n[2] - Sair do programa")

while True:
    exibirMenu()
    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        carac = int(input("Informe a quantidade de caracteres, lembrando que o mínimo deve ser de 8: "))

        while carac < 8:
            carac = int(input("A quantidade mínima é de 8 caracteres, tente novamente: "))

        qnt = int(input("Informe a quantidade de senhas a serem geradas: "))
        print(f"\nForam geradas um total de {qnt} senhas com sucesso. Veja abaixo: ")

        for x in range(qnt):
            password = ''.join(random.choice(chars) for z in range(carac))
            print(password)

    elif opcao == 2:
        print("Encerrando o programa, até mais.")
        break

    else:
        print("Opção inválida, tente novamente.")
        print("--------------------------------")
