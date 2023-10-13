import random as rd
import time
import matplotlib.pyplot as plt
import numpy as np

tTOTALs = time.time()


# Criação da lista
def ListaRepElem(n: int) -> list:
    lista = []
    for i in range(n - 1):
        lista.append(i + 1)

    rd.shuffle(lista)

    lista.insert(rd.choice(lista), rd.randint(0, n + 1))
    return lista


# Algoritmos
def SolExaustiva(lista: list):  # 2 + N^2
    start = time.time()
    # i = 0        N
    for i in range(len(lista)):
        # j = 0         i+1     N
        for j in range(i + 1, len(lista)):
            # 1
            if lista[i] == lista[j]:  # 1

                end = time.time()

                return end - start


def SolSort(lista: list):
    start = time.time()
    lista.sort()

    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            end = time.time()

            return end - start


def SolSoma(lista: list) -> float:
    start = time.time()

    n = len(lista) - 1
    SomaPA = (1 + n) * n / 2

    SomaLst = 0
    for i in range(len(lista)):
        SomaLst += lista[i]

    elem = SomaLst - SomaPA

    end = time.time()

    return end - start


# ------------------------------------------------ AUX FUNCTIONS -------------------------------------------------------
def MeanList(lista: list) -> float:
    soma = 0

    for elem in lista:
        soma += elem

    return soma / len(lista)


def MedianDicts(dic: dict):
    nDic = {}
    for k, v in dic:
        nDic[k] = np.median(v)

    return nDic


# ------------------------------------------------ EXPERIMENTAÇÃO ------------------------------------------------------
lstArraySizes = [20000, 40000, 60000, 80000, 100000]  # 20000, 40000, 60000, 80000, 100000


def Testes(nTestes: int, arrayList: list):
    lstTExaut = []
    lstTSort = []
    lstTSoma = []

    dicExaust = {}
    dicSort = {}
    dicSoma = {}

    dicMeanExeust = {}
    dicMeanSort = {}
    dicMeanSoma = {}

    plt.figure()

    for elem in arrayList:
        tExau = []
        tSoma = []
        tSort = []
        for i in range(nTestes):
            lst = ListaRepElem(elem)
            tExau.append(SolExaustiva(lst))
            tSort.append(SolSort(lst))
            tSoma.append(SolSoma(lst))

        dicExaust[elem] = tExau
        dicSort[elem] = tSort
        dicSoma[elem] = tSoma

        lstTExaut.append(MeanList(tExau))
        dicMeanSort[elem] = lstTSort.append(MeanList(tSort))
        dicMeanSoma[elem] = lstTSoma.append(MeanList(tSoma))

        print("\n============ DADOS DE EXECUCAO ============")
        print(f"Numero de amostragem = {nTestes}. ArraySize = {elem}\n")
        print(f"Média de tempo de SolExaust: {MeanList(tExau)}")
        print(f"Média de tempo de SolSort: {MeanList(tSort)}")
        print(f"Média de tempo de SolSoma: {MeanList(tSoma)}")

    print(f"\nExaustao {lstTExaut}")
    print(f"Sort {lstTSort}")
    print(f"Soma {lstTSoma}")

    plt.plot(lstArraySizes, lstTExaut, color='b', marker='o', label='exaustiva')
    plt.plot(lstArraySizes, lstTSort, color='r', marker='*', label='Sort')
    plt.plot(lstArraySizes, lstTSoma, color='g', marker='o', linestyle='dashed', label='Soma')

    plt.xlabel('Array Size (n)')
    plt.ylabel('Tempo')

    plt.legend()
    plt.show()

    return dicExaust, dicSort, dicSoma


dicExau, dicSor, dicSum = Testes(1, lstArraySizes)

print(f"Dic Exaust: {MedianDicts(dicExau)}")
print(f"Dic Sort: {MedianDicts(dicSor)}")
print(f"Dic Soma: {MedianDicts(dicSum)}")

tTOTALf = time.time()
print(f"\nTEMPO TOTAL: {tTOTALf - tTOTALs}")
