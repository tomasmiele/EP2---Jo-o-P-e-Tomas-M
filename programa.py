from funcoes import *
import json

with open('paises.json', 'r') as arquivo:
  texto = arquivo.read()

dicio_paises = json.loads(texto)

raio_terra = 6371

DADOS_CONVERTIDOS = normaliza(dicio_paises['DADOS'])

tentativas = 20
distancias = [] 
dicas = []


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
  elif palpite == 'dica':
    ops = '0'
    print('\nMercado de Dicas')
    print('---------------------------------------------')
    if tentativas > 4:
      print('1. Cor da bandeira - custa 4 tentativas')
      ops = ops + '|1'
    if tentativas > 3:
      print('2. Letra da capital - custa 3 tentativas')
      ops = ops + '|2'
    if tentativas > 6:
      print('3. Área - custa 6 tentativas')
      ops = ops + '|3'
    if tentativas > 5:
      print('4. População - custa 5 tentativas')
      ops = ops + '|4'
    if tentativas > 7:
      print('5. Continente - custa 7 tentativas')
      ops = ops + '|5'
    print('0. Sem dica')
    print('---------------------------------------------')
    if len(ops) > 1:
      ops = 'Escolha sua opção [' + ops + ']: '
      dica_opcao = int(input(ops))
    else:
      print('>>> Infelizmente, acabou seu estoque de dicas! <<<')
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