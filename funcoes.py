#importacoes
import random
import math

#normalizando base de país
def normaliza(paises):
    dicio = {}
    for chave, valor in paises.items():
        for chave2, valor2 in valor.items():
            dicio[chave2] = valor2
            dicio[chave2]['continente'] = chave
    return dicio

#sorteando países
def sorteia_pais(paises):
    chaves = []
    for i in paises.keys():
        chaves.append(i)
    return random.choice(chaves)

#distância haversine
def haversine(r, phi1, lambda1, phi2, lambda2):
    d = (2*r)*(math.asin(math.sqrt((((math.sin(math.radians((phi2-phi1)/2)))**2) + math.cos(math.radians(phi1)) * math.cos(math.radians(phi2)) * ((math.sin(math.radians((lambda2-lambda1)/2)))**2)))))
    return d

#adicionando em uma lista ordenada
def adiciona_em_ordem(pais, dist, lista_p):
    adicionar = [pais, dist]
    lista_v = []
    if lista_p == lista_v:
        lista_v.append(adicionar)
        return lista_v
    else:
        for p in range(len(lista_p)):
            if dist > lista_p[p][1]:
                lista_v.append(lista_p[p])
            else:
                lista_v.append(adicionar)
                lista_v.append(lista_p[p])
                dist = lista_p[-1][1]+1
        
        if adicionar not in lista_v:
            lista_v.append(adicionar)
        return lista_v

#está na lista
def esta_na_lista(pais, lista_p):
    resp = False
    for i in range(len(lista_p)):
        if pais == lista_p[i][0]:
            resp = True
            
    return resp


#sorteia letra com restricoes
def sorteia_letra(palavra, letras_f):
    caract = ['.', ',', '-', ';', ' ']
    saida = []
    vazio = ''
    palavra = palavra.lower()
    for p in palavra:
        if p not in letras_f and p not in caract and p not in saida:
            saida.append(p)
    if saida == []:
        return vazio
    else: 
        sorteio = random.choice(saida)
        return sorteio

