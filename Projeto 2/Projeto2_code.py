import random as rd
import time


# Criação da lista
def ListaRepElem(n: int) -> list:
    lista = []
    for i in range(n - 1):
        lista.append(i + 1)

    rd.shuffle(lista)

    lista.insert(rd.choice(lista), rd.randint(0, n + 1))
    return lista


# lst = ListaRepElem(1000)  # Comprimento array


def SolExaustiva(lista: list) -> float:
    start = time.time()

    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] == lista[j] and i != j:
                end = time.time()
                t = end - start

                print("\n--------- SOLUCAO EXAUSTIVA ---------")
                print(f"O valor repetido eh {lista[i]}, e esta nas posicoes {i} e {j}")
                print(f"TEMPO DE EXECUCAO: {t}")
                return t


def SolSort(lista: list) -> float:
    start = time.time()
    lista.sort()

    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            end = time.time()
            t = end - start

            print("\n--------- SOLUCAO POR SORT ---------")
            print(f"O valor repetido eh {lista[i]}, e esta nas posicoes {i} e {i + 1}")
            print(f"TEMPO DE EXECUCAO: {t}")
            return t


def SolSoma(lista: list) -> float:
    start = time.time()

    n = len(lista) - 1
    SomaPA = (1 + n) * n / 2

    SomaLst = 0
    for i in range(len(lista)):
        SomaLst += lista[i]

    elem = SomaLst - SomaPA

    end = time.time()
    t = end - start

    print("\n--------- SOLUCAO POR SOMA ---------")
    print(f"O valor repetido eh {elem}")
    print(f"TEMPO DE EXECUCAO: {t}")

    return t


# ------------------------------------------------ AUX FUNCTIONS -------------------------------------------------------
def MeanList(lista: list) -> float:
    soma = 0

    for elem in lista:
        soma += elem

    return soma / len(lista)


# ------------------------------------------------ EXPERIMENTAÇÃO ------------------------------------------------------
def Testes(nTestes: int, arraySize: int):
    tExau = []
    tSoma = []
    tSort = []

    for i in range(nTestes):
        print(f"\n========== {i} ==========")
        lst = ListaRepElem(arraySize)

        tExau.append(SolExaustiva(lst))
        tSort.append(SolSort(lst))
        tSoma.append(SolSoma(lst))


Testes(3, 1000)
