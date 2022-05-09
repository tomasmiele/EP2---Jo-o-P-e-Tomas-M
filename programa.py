from funcoes import *
import json

with open('paises.json', 'r') as arquivo:
  texto = arquivo.read()

dicio_paises = json.loads(texto)

raio_terra = 6371

DADOS_CONVERTIDOS = normaliza(dicio_paises['DADOS'])

tentativas = 20
distancias = []

pais_sorteado = sorteia_pais(DADOS_CONVERTIDOS)
latitude_pais_sorteado = DADOS_CONVERTIDOS[pais_sorteado]['geo']['latitude']
longitude_pais_sorteado = DADOS_CONVERTIDOS[pais_sorteado]['geo']['longitude']

print(pais_sorteado)

while tentativas != 0:
  if distancias != []:
    print('\nDistâncias:')
    for i in range(len(distancias)):
      print(distancias[i][1], 'km ->', distancias[i][0])
  
  print('\nVocê tem', tentativas, 'tentativa(s) \n')
  palpite = input('Qual o seu palpite? ')

  esta = False
  for chave in DADOS_CONVERTIDOS.keys():
    if chave == palpite:
      esta = True

  if palpite == 'desisto':
    desistir = input('Tem certeza que deseja desistir da rodada? [s|n] ')
    if desistir == 'n':
      continue
    elif desistir == 's':
      print('Que deselegante desistir, o pais era:', pais_sorteado)
      break
    else:
      print('país desconhecido \n')
  #elif palpite == 'dica':
    #fazer as dicas
  #elif palpite == 'inventario':
    #fazer o inventario
  elif esta == True:
    latitude_palpite = DADOS_CONVERTIDOS[palpite]['geo']['latitude']
    longitude_palpite = DADOS_CONVERTIDOS[palpite]['geo']['longitude']
    kilometros = haversine(raio_terra, latitude_pais_sorteado, longitude_pais_sorteado, latitude_palpite, longitude_palpite)
    esta_distancias = esta_na_lista(palpite, distancias)
    if kilometros != 0:
      if esta_distancias == False:
        arredondar = round(kilometros, 0)
        distancias = adiciona_em_ordem(palpite, arredondar, distancias)
        tentativas -= 1
      elif esta_distancias == True:
        tentativas -= 1
    else:
      tentativas -= 1
      print('*** Parabéns! Você acertou após', 20-tentativas, 'tentativas!\n')
      break
  else:
    print('país desconhecido')