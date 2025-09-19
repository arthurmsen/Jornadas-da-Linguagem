import random
import time

print ('Jogo da velha')

while True:
  msg1 = input ('Gostaria de jogar? ')
  msg1 = msg1.lower()
  if msg1 != 'sim':
    break
  print ('')  
  print ('O tabuleiro é o seguinte (cada número indica a posição da casa):')
  print ('')
  print (' 1 | 2 | 3 ')
  print ('---+---+---')
  print (' 4 | 5 | 6 ')
  print ('---+---+---')
  print (' 7 | 8 | 9 ')
  print ('')
  lista1 = [' ', ' ', ' ']
  lista2 = [' ', ' ', ' ']
  lista3 = [' ', ' ', ' ']
  posicoesusadas = []
  terminou = 1
  jogadas = 8
  simbolos = ['X', 'O']
  msg2 = input ('Escolha com qual símbolo você quer jogar, X ou O: ')
  if msg2 == '':
    print ('')
    msg0 = input ('Deseja ainda continuar jogando? ')
    msg0 = msg0.lower()
    if msg0 != 'sim':
      break
    print ('')
    continue  
  simbolo = msg2.upper()
  if simbolo not in simbolos:
    print ('')
    print ('Por favor, escolha o símbolo correto.')
    print ('')
    continue
  simbolos.remove(simbolo)
  simbolo2 = simbolos[0]  
  print ('')  

  while True:
    escolha = input ('Escolha qual posição você deseja jogar (de 1 a 9): ')
    if escolha == '':
      print ('')
      msg0 = input ('Deseja ainda continuar jogando? ')
      msg0 = msg0.lower()
      if msg0 != 'sim':
        break
      print ('')
      continue  
    if escolha in posicoesusadas:
      print ('')
      print ('Por favor, escolha uma posição ainda não utilizada.')
      print ('')
      continue
    if escolha not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
      print ('')
      print ('Por favor, escolha a posição correta.')
      print ('')
      continue
    posicoesusadas.append (escolha)  

    if escolha == '1':
      lista1[0] = simbolo
    elif escolha == '2':
      lista1[1] = simbolo
    elif escolha == '3':
      lista1[2] = simbolo
    elif escolha == '4':
      lista2[0] = simbolo
    elif escolha == '5':
      lista2[1] = simbolo
    elif escolha == '6':
      lista2[2] = simbolo
    elif escolha == '7':
      lista3[0] = simbolo
    elif escolha == '8':
      lista3[1] = simbolo
    else:
      lista3[2] = simbolo

    print ('')
    print ('Agora, o computador está sorteando a posição, aguarde.')
    print ('')
    espera = ''
    for numero in range (6):
      espera += '*'
      print (espera)
      time.sleep (0.5)

    while True:
      computador = random.randint (1, 9)
      computador =  str (computador)
      if computador in posicoesusadas:
        continue  
      print ('')
      posicoesusadas.append(computador)
      break
   
    if computador == '1':
      lista1[0] = simbolo2
    elif computador == '2':
      lista1[1] = simbolo2
    elif computador == '3':
      lista1[2] = simbolo2
    elif computador == '4':
      lista2[0] = simbolo2
    elif computador == '5':
      lista2[1] = simbolo2
    elif computador == '6':
      lista2[2] = simbolo2
    elif computador == '7':
      lista3[0] = simbolo2
    elif computador == '8':
      lista3[1] = simbolo2
    else:
      lista3[2] = simbolo2
    jogadas -= 2  

    while jogadas > 0:
      for i in range (3):
        if lista1[i] == lista2[i] and lista1[i] != ' ':
          if lista2[i] == lista3[i]:
            terminou = 0
            if lista3[i] == simbolo:
              print ('Parabéns, você ganhou!')
              print ('')
            else:
              print ('Que pena! Não foi dessa vez...')
              print ('')
      if lista1[0] == lista1[1] and lista1[0] != ' ':
        if lista1[1] == lista1[2]:
          terminou = 0
          if lista1[0] == simbolo:
            print ('Parabéns, você ganhou!')
            print ('')
          else:
            print ('Que pena! Não foi dessa vez...')
            print ('')
      if lista2[0] == lista2[1] and lista2[0] != ' ':
        if lista2[1] == lista2[2]:
          terminou = 0
          if lista2[0] == simbolo:
            print ('Parabéns, você ganhou!')
            print ('')
          else:
            print ('Que pena! Não foi dessa vez...')
            print ('')
      if lista3[0] == lista3[1] and lista3[0] != ' ':
        if lista3[1] == lista3[2]:
          terminou = 0
          if lista3[0] == simbolo:
            print ('Parabéns, você ganhou!')
            print ('')
          else:
            print ('Que pena! Não foi dessa vez...')
            print ('')
      if lista1[0] == lista2[1] and lista1[0] != ' ':
        if lista2[1] == lista3[2]:
          terminou = 0
          if lista3[2] == simbolo:
            print ('Parabéns, você ganhou!')
            print ('')
          else:
            print ('Que pena! Não foi dessa vez...')
            print ('')
      if lista1[2] == lista2[1] and lista1[2] != ' ':
        if lista2[1] == lista3[0]:
          terminou = 0
          if lista3[0] == simbolo:
            print ('Parabéns, você ganhou!')
            print ('')
          else:
            print ('Que pena! Não foi dessa vez...')
            print ('')
      break

    if terminou == 0:
      break
    elif jogadas == 0:
      print ('Ocorreu empate no jogo.')
      print ('')
      break
    else:
      print ('Agora, o tabuleiro está assim:')
      print ('')
      print (' ' + lista1[0] + ' | ' + lista1[1] + ' | ' + lista1[2] + ' ')
      print ('---+---+---')
      print (' ' + lista2[0] + ' | ' + lista2[1] + ' | ' + lista2[2] + ' ')
      print ('---+---+---')
      print (' ' + lista3[0] + ' | ' + lista3[1] + ' | ' + lista3[2] + ' ')
      print ('')
      continue
