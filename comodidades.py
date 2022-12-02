import os
from time import sleep

linha = "=" * 50
clear = lambda: os.system("cls")


def center(value):
    centralizar = str(len(value) / 2)
    verificar = centralizar.split(".")
    diminuir = len(value) / 2

    if verificar[1] == "5":
        diminuir = diminuir + 0.5
        return print(" " * int((25.0 - diminuir)) + value)
    else:
        return print(" " * int((25.0 - diminuir)) + value)