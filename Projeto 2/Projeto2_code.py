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


# Algoritmos
def SolExaustiva(lista: list) -> float:
    start = time.time()

    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] == lista[j] and i != j:
                end = time.time()
                t = end - start

                return t


def SolSort(lista: list) -> float:
    start = time.time()
    lista.sort()

    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            end = time.time()
            t = end - start

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

    return t


# ------------------------------------------------ AUX FUNCTIONS -------------------------------------------------------
def MeanList(lista: list) -> float:
    soma = 0

    for elem in lista:
        soma += elem

    return soma / len(lista)


# ------------------------------------------------ EXPERIMENTAÇÃO ------------------------------------------------------
lstArraySizes = [20000, 40000, 60000, 80000, 100000]


def Testes(nTestes: int, arrayList: list):
    tExau = []
    tSoma = []
    tSort = []

    for elem in arrayList:
        for i in range(nTestes):
            lst = ListaRepElem(elem)

            tExau.append(SolExaustiva(lst))
            tSort.append(SolSort(lst))
            tSoma.append(SolSoma(lst))

        print("\n============ DADOS DE EXECUCAO ============")
        print(f"Numero de amostragem = {nTestes}. ArraySize = {elem}\n")
        print(f"Média de tempo de SolExaust: {MeanList(tExau)}")
        print(f"Média de tempo de SolSort: {MeanList(tSort)}")
        print(f"Média de tempo de SolSoma: {MeanList(tSoma)}")


Testes(1, lstArraySizes)