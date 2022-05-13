from funcoes import *
import json
import random

with open('paises.json', 'r') as arquivo:
  texto = arquivo.read()

dicio_paises = json.loads(texto)

raio_terra = 6371

DADOS_CONVERTIDOS = normaliza(dicio_paises['DADOS'])

class bcolors:
  cinza = '\033[1;30m'
  roxo = '\033[0;35m'
  vermelho = '\033[0;31m'
  amarelo = '\033[1;33m'
  azul_claro = '\033[1;36m'
  cor_normal = '\033[0m'

print(' ============================ ')
print('|                            |')
print('| BEM VINDO AO INSPER PAÍSES |')
print('|                            |')
print(' ==== DESIGN DE SOFTWARE ==== ')
print('\nComandos:')
print('\n    dica       - entra no mercado de dicas')
print('    desisto    - desiste da rodada')
print('    inventario - exibe sua posição')

continuar_jogando = True

while continuar_jogando == True:
  tentativas = 20
  distancias = [] 
  dicas = []
  cores = []
  cores_sorteadas = []
  letras_restritas = []

  pais_sorteado = sorteia_pais(DADOS_CONVERTIDOS)
  latitude_pais_sorteado = DADOS_CONVERTIDOS[pais_sorteado]['geo']['latitude']
  longitude_pais_sorteado = DADOS_CONVERTIDOS[pais_sorteado]['geo']['longitude']
  for chave in  DADOS_CONVERTIDOS[pais_sorteado]['bandeira'].keys():
    if DADOS_CONVERTIDOS[pais_sorteado]['bandeira'][chave] > 0 and chave != 'outras':
      cores.append(chave)
  capital = DADOS_CONVERTIDOS[pais_sorteado]['capital']
  tamanho_capital = len(capital)
  dica3_ja_foi_escolhida = False
  dica4_ja_foi_escolhida = False
  dica5_ja_foi_escolhida = False
  ganhou = False
  inventario = True

  while tentativas != 0:
    if tentativas > 10:
      tenta_cor = bcolors.azul_claro + str(tentativas) + bcolors.cor_normal
    elif tentativas <= 10 and tentativas > 5:
      tenta_cor = bcolors.amarelo+ str(tentativas) + bcolors.cor_normal
    elif tentativas <= 5:
      tenta_cor = bcolors.vermelho + str(tentativas) + bcolors.cor_normal

    if inventario == False:
      print('\nDistâncias:')
      for i in range(len(distancias)):
        if distancias[i][1] >= 10000:
          print(bcolors.cinza + str(distancias[i][1]), 'km ->', distancias[i][0] + bcolors.cor_normal)
        elif distancias[i][1] < 10000 and distancias[i][1] >= 5000:
          print(bcolors.roxo + str(distancias[i][1]), 'km ->', distancias[i][0] + bcolors.cor_normal)
        elif distancias[i][1] < 5000 and distancias[i][1] >= 2000:
          print(bcolors.vermelho + str(distancias[i][1]), 'km ->', distancias[i][0] + bcolors.cor_normal)
        elif distancias[i][1] < 2000 and distancias[i][1] >= 1000:
          print(bcolors.amarelo + str(distancias[i][1]), 'km ->', distancias[i][0] + bcolors.cor_normal)
        elif distancias[i][1] < 1000:
          print(bcolors.azul_claro + str(distancias[i][1]), 'km ->', distancias[i][0] + bcolors.cor_normal)
  
      print('\nDicas: ')
      for i in range(len(dicas)):
        print(dicas[i])
    inventario = False

    print('\nVocê tem',tenta_cor, 'tentativa(s) \n')
    palpite = input('Qual o seu palpite? ').lower()

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
      if tentativas > 6 and dica3_ja_foi_escolhida == False:
        print('3. Área - custa 6 tentativas')
        ops = ops + '|3'
      if tentativas > 5 and dica4_ja_foi_escolhida == False:
        print('4. População - custa 5 tentativas')
        ops = ops + '|4'
      if tentativas > 7 and dica5_ja_foi_escolhida == False:
        print('5. Continente - custa 7 tentativas')
        ops = ops + '|5'
      print('0. Sem dica')
      print('---------------------------------------------')
      if len(ops) > 1:
        ops = 'Escolha sua opção [' + ops + ']: '
        dica_opcao = int(input(ops))
      else:
        print('>>> Infelizmente, acabou seu estoque de dicas! <<<')
        dica_opcao = 0
      if dica_opcao == 0:
        continue
      elif dica_opcao == 1:
        if len(cores) > 0:
          tentativas -= 4
          cores_sorteadas.append(random.choice(cores))
          cores.remove(cores_sorteadas[-1])
          if len(cores_sorteadas) == 1:
            cores_bandeira = '-Cores da bandeira: ' + str(cores_sorteadas[0])
            dicas.append(cores_bandeira)
            aonde_cores = dicas.index(cores_bandeira)
          elif len(cores_sorteadas) > 1:
            cores_bandeira = '-Cores da bandeira: ' + str(cores_sorteadas[0])
            for i in range(1, len(cores_sorteadas)):
              cores_bandeira = cores_bandeira + ', ' + str(cores_sorteadas[i]) 
            dicas[aonde_cores] = cores_bandeira
        elif len(cores) == 0:
          print('Cores esgotadas!')
          continue
      elif dica_opcao == 2:
        if tamanho_capital > 0:
          tentativas -= 3
          letra_sorteada = sorteia_letra(capital, letras_restritas)
          conta_letras = 0
          for i in range(len(capital)):
            if capital[i].lower() == letra_sorteada:
                conta_letras += 1
          tamanho_capital -= conta_letras
          letras_restritas.append(letra_sorteada)
          letras_capital = '- Letras da capital: '
          if len(letras_restritas) == 1:
            letras_capital += letras_restritas[0]
            dicas.append(letras_capital)
            aonde_letra_capital = dicas.index(letras_capital)
          elif len(letras_restritas) > 1:
            letras_capital += letras_restritas[0]
            for i in range(1, len(letras_restritas)):
              letras_capital = letras_capital + ', ' + str(letras_restritas[i])
            dicas[aonde_letra_capital] = letras_capital
        elif tamanho_capital == 0:
          print('Letras esgotadas!')
          continue
      elif dica_opcao == 3:
        area = '- Área: ' + str(DADOS_CONVERTIDOS[pais_sorteado]['area']) + ' km2'
        if dica3_ja_foi_escolhida == True:
          print('Opção inválida')
        else:
          dica3_ja_foi_escolhida = True
          dicas.append(area)
          tentativas -= 6
      elif dica_opcao == 4:
        populacao = '- População: ' + str(DADOS_CONVERTIDOS[pais_sorteado]['populacao']) + ' habitantes'
        if dica4_ja_foi_escolhida == True:
          print('Opção inválida')
        else:
          dica4_ja_foi_escolhida = True
          dicas.append(populacao)
          tentativas -= 5
      elif dica_opcao == 5:
        continente = '- Continente: ' + str(DADOS_CONVERTIDOS[pais_sorteado]['continente']) 
        if dica5_ja_foi_escolhida == True:
          print('Opção inválida')
        else:
          dica5_ja_foi_escolhida = True
          dicas.append(continente)
          tentativas -= 7
    elif palpite == 'inventario':
      inventario  = True
      print('\nDistâncias:')
      for i in range(len(distancias)):
        print(distancias[i][1], 'km ->', distancias[i][0])
  
      print('\nDicas: ')
      for i in range(len(dicas)):
        print(dicas[i])
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
        ganhou = True
        break
    else:
      print('país desconhecido')
  if ganhou == True:
    continuar_jogando = input('\nJogar novamente? [s|n] ')
    if continuar_jogando == 's':
      continuar_jogando = True
    elif continuar_jogando == 'n':
      continuar_jogando = False
  elif ganhou == False:
    print('>>> Você perdeu, o país era:', pais_sorteado)
    continuar_jogando = input('\nJogar novamente? [s|n] ')
    if continuar_jogando == 's':
      continuar_jogando = True
    elif continuar_jogando == 'n':
      continuar_jogando = False
print('\n\n\nAté a próxima!')