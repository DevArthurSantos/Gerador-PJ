from comodidades import *
import random

def nomes():
    with open("nomes.csv", "r") as file:
        lines = [line.strip() for line in file]
        nome = f"{lines[random.randrange(0, len(lines), 2)]} {lines[random.randrange(0, len(lines), 2)]}"
        return nome


def telefone():

    ddd = str(random.randint(3, 6)) + str(random.randint(6, 9))
    telNumero = ""
    for i in range(9):
        telNumero += str(random.randint(3, 8))
        if i == 4:
            telNumero += "-"
    telefone = f"({ddd}) 9 {telNumero}"
    return telefone


def CPF():

    cpfNumero = ""
    for i in range(11):
        cpfNumero += str(random.randint(3, 8))
        if i == 2 or i == 5:
            cpfNumero += "."
        if i == 8:
            cpfNumero += "-"
    cpf = f"{cpfNumero}"
    return cpf


def RG():

    rgNumero = ""
    for i in range(7):
        rgNumero += str(random.randint(3, 8))
        if i == 0 or i == 3:
            rgNumero += "."
    rg = f"{rgNumero}"
    return rg


def gerarNome():
    newNome = nomes()
    clear()
    print(linha)
    print(f"Nome: {newNome}")
    print(linha)


def gerarCPF():
    newCPF = CPF()
    clear()
    print(linha)
    print(f"CPF: {newCPF}")
    print(linha)


def gerarTelefone():
    newTelefone = telefone()
    clear()
    print(linha)
    print(f"Tel: {newTelefone}")
    print(linha)


def gerarRG():
    newRG = RG()
    clear()
    print(linha)
    print(f"RG: {newRG}")
    print(linha)


def gerarTudo():
    clear()
    print(linha)
    newNome = nomes()
    newCPF = CPF()
    newTelefone = telefone()
    newRG = RG()
    print(f"Nome: {newNome}")
    print(f"RG:   {newRG}")
    print(f"CPF:  {newCPF}")
    print(f"Tel:  {newTelefone}")
    print(linha)
