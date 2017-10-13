def validaTipoItem(a):
    if a == 'documento' or a == 'pacote':
        res = 'true'
    else:
        res = 'false'
    return (res)

def validaPeso(b):
    if b >= 0:
        res = 'true'
    else:
        res = 'false'
    return(res)

def convertePeso(c):
    n = (c * 1000)
    return(n)

def calculaCustoItem(a,d):
    if a == 'documento':
        n = d * 2.00
    elif a == 'pacote':
        n = d * 3.00
    return(n)

def validaEmbalagem(e):
    if e == 'pequena' or e == 'média' or e == 'media' or e == 'grande':
        res = 'True'
    else:
        res = 'False'
    return(res)
def calculaCursoEmbalagem(e):
    if e == 'pequena':
        preco = 4
    elif e == 'média' or e == media:
        preco = 7
    elif e == 'grande':
        preco = 10
    else:
        preco = 'Embalagem inválida'
    return preco
def calculaCustoEntrega(f):
    if f == 'normal':
        ac = 0
    elif f == 'sedex':
        ac = 5
    elif f == 'sedex 10':
        ac = 8
    else:
        ac = 'Modo de entrega inválido'
    return ac



