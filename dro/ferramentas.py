
from math import ceil, radians, tau, cos, sin
import itertools


##calcular furos ao raio
def calcFurosAoRaio(furos, raio, desloc):
    desloc = radians(desloc)
    angulo = tau / furos

    lista = [(
        cos(i * angulo + desloc)*raio  ,
        sin(i * angulo + desloc)*raio  )
        for i in range(furos)]

    return lista


##calcular furos a diagonal
def calcFurosADiagonal(furos, angulo, espaco, desloc):
    angulo = radians(angulo)

    lista = [(
        cos(angulo)*(i*espaco + desloc)  ,
        sin(angulo)*(i*espaco + desloc)  )
        for i in range(furos)]

    return lista


##emmPafinasDe
def emPaginasDe(lista, n=1):
    for index in range(ceil(len(lista) / n)):
        yield itertools.islice(lista, index*n, index*n+n)


##pegarPagina
def pegarPagina(lista, n=1, pagina=1):
    if not pagina: return []
    return itertools.islice(lista, n*(pagina-1), n*pagina)

