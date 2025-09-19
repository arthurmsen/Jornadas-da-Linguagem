print ('Jogo da senha - Introdução')
print ('')
print ('Seja bem-vindo ao jogo da senha! Nesse jogo, o computador seleciona aleatoriamente um número de três algarismos distintos. A tarefa do jogador é tentar adivinhar qual é esse número. Para isso, o computador dispõe dicas ao usuário, informando se um dos três algarismos está certo, trocado ou errado (não necessariamente na ordem em que aparecem). Vamos começar?')
print ('')

import random
from random import choice
import time

nome = input ('Qual seu nome, jogador? ')
if nome == '':
  print ('Por favor, informe seu nome para prosseguir.')
print ('')
while True:
  msg2 = input ('Pronto para jogar? ')
  msg2 = msg2.lower()
  if msg2 != 'sim':
    break
  print ('')
  print ('O computador está sorteando o número, aguarde.')
  lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  centena = choice (lista)
  while centena == '0':
    centena = choice (lista)     
  dezena = choice (lista)
  while dezena == centena:
    dezena = choice (lista)
  unidade = choice (lista)
  while unidade == dezena or unidade == centena:
    unidade = choice (lista) 
  numero = []  
  numero.append(centena)
  numero.append(dezena)
  numero.append(unidade)
  print ('')
  espera = ''
  for i in range (6):
    espera += '*'
    print (espera)
    time.sleep(0.5)
  print ('')
  print ('Tudo certo! O computador já escolheu o número.')
  print ('')
  while True:
    dicas  = []
    escolha = input ('Escolha um número: ')
    print ('')
    if escolha == '':
      msg3 = input ('Deseja continuar jogando? ')
      msg3= msg3.lower()
      if msg3 == 'sim':
        print ('')
        continue
      else:
        break  
    inicio = 0
    escolha = list (escolha)
    tamanho = len (escolha)
    tamanho = int (tamanho)
    if tamanho != 3:
      print ('Por favor, digite um número de somente três algarismos.')
      print ('')
      continue  
    while tamanho > 0:
      if escolha[inicio] in numero:
        if escolha[inicio] == numero[inicio]:
          dicas.append('Certo')
        else:
          dicas.append('Trocado')
      else:
        dicas.append('Errado')
      inicio = inicio + 1
      tamanho = tamanho - 1
    random.shuffle(dicas)
    if dicas[0] == 'Certo':
      if dicas[1] == 'Certo':
        if dicas[2] == 'Certo':
          print ('Parabéns ' + nome + ', você ganhou!')  
          print ('')
          break
    else:
      print ('As dicas do computador são:')
      print ('')
      for a in range (3):
        print (dicas[a])
      print ('')  
