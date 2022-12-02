from comodidades import *
from gerar import *

def menuPrincipal():
    while True:
        clear()
        print(linha)
        center("Menu Princial")
        print(linha)
        print("[1] Gerar tudo")
        print("[2] Gerar nome")
        print("[3] Gerar cpf")
        print("[4] Gerar telefone")
        print("[5] Gerar rg")
        print(linha)
        opcao = input("Numero da escolha: ")
        if opcao == "1":
            gerarTudo()
            break
        elif opcao == "2":
            gerarNome()
            break
        elif opcao == "3":
            gerarCPF()
            break
        elif opcao == "4":
            gerarTelefone()
            break
        elif opcao == "5":
            gerarRG()
            break
        else:
            for i in range(6):
                clear()
                print(linha)
                print(f"altarnativa invalida tente novamente {i}s...")
                print(linha)
                sleep(1)