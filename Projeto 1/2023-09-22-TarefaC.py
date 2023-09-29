

def substituicoes (entrada):
    saida = entrada
    saida = saida.replace("IV", "IIII")
    saida = saida.replace("IX", "VIIII")
    saida = saida.replace("XL", "XXXX")
    saida = saida.replace("XC", "LXXXX")
    saida = saida.replace("CD", "CCCC")
    saida = saida.replace("CM", "DCCCC")
    return saida


algarismos={"I":1, "V":5, "X":10, "L": 50, "C": 100, "D":500, "M": 1000}
composicao = {}

entrada = "MCMLXXIV"
temp = substituicoes (entrada)

for i in temp:
    composicao[i]= composicao.setdefault(i, 0) + 1
    
saida = 0
for k,v in composicao.items():
    saida = saida + (v * algarismos.get(k))
    