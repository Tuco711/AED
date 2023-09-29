def processa(valor, passo):
    
    if valor % 2 == 0:
        novoValor = (valor / 2)
    else :
        novoValor = (valor - 1)
        
    if valor == 0:
        return passo
    
    return processa(novoValor, passo+1)

processa (14, 0)
6
processa (13, 0)
6
processa (12, 0)