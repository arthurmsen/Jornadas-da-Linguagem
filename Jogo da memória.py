import random as rd
import time

def montaPares (nPares):
  simbolo = ''
  lista = []
  for numero in range (33, 33 + nPares):
    simbolo = simbolo + chr (numero)
    lista.append(simbolo)
  lista2 = lista.copy()
  listafinal = lista + lista2
  rd.shuffle(listafinal)
  return listafinal

def montaTela(nPares):
  linha1 = '+'
  linha2 = '|'
  linha3 = '|'
  for numero in range (1, 2*nPares + 1):
    linha1 += '-+'
    dez = numero // 10
    if dez == 0:
      linha2 += ' |'
    else:
      linha2 += str(dez) + '|'
    uni = numero % 10
    linha3 += str(uni) + '|'
  print (linha1)
  print (linha2)
  print (linha3)  
  return linha1

def mascaraInicial(nPares):
  linha5 = ' '
  for numero in range (1, 2*nPares + 1):
    linha5 += '*'
    linha5 += ' '
  return linha5

print ('Jogo da Memória - Introdução')
print ('')
print ('Seja bem-vindo ao jogo da memória! Nesse jogo, serão apresentados diferentes pares de símbolos, e sua função é identificar os pares com o mesmo símbolo em diferentes posições. Vamos começar?')
print ('')
nome = input ('Digite seu nome: ')
while True:
  msg1 = input (nome + ', gostaria de jogar? ')
  msg1 = msg1.lower()
  if msg1 != 'sim':
    break
  print ('')
  msg2 = input ('Escolha com quantos pares deseja jogar: ')
  if msg2 == '':
    print ('Quantidade de pares inválida.')
    print ('')
    continue
  print ('')
  nPares = int (msg2) 
  simbolos = montaPares (nPares)
  mascara = mascaraInicial (nPares)
  palpitesdados = []
  print ('O total de pares de símbolos é esse:')
  print ('')
  print (montaTela(nPares))
  print (mascara)
  print ('')
  while True:
    msg3 = input ('Escolha uma posição para virar (de 1 a ' + str (nPares*2) + '): ')
    if msg3== '':
      msg3 = input ('Deseja parar o programa? ')
      msg3 = msg3.lower()
      if msg3 == 'sim' or msg3 != 'não':
        print ('')
        break
      else:
        print ('')
        continue
    palpite1 = int (msg3)  
    if palpite1 <= 0 or palpite1 > len (simbolos):
      print ('Escolha uma posição correta a ser virada.')
      print ('')
    palpitesdados.append(palpite1)  
    mascara2 = list (mascara)
    msg4 = input ('Agora, escolha outra posição para virar: ')
    print ('')
    if msg4 == '':
      msg4 = input ('Deseja parar o programa? ')
      msg4 = msg4.lower()
      if msg4 == 'sim' or msg4 != 'não':
        print ('')
        break
      else:
        print ('')
        continue
    palpite2 = int (msg4)
    if palpite2 in palpitesdados:
      print ('Escolha uma posição que ainda não foi virada.')
      print ('')
    if palpite2 <= 0 or palpite2 > len (simbolos):
      print ('Escolha uma posição correta a ser virada.')
      print ('')                    
    if simbolos[palpite1 - 1] == simbolos[palpite2 - 1]:
      time.sleep(1.5)
      palpitesdados.append(palpite2)
      print ('Boa escolha! Agora, os pares de símbolos estão assim:')
      print ('')
      mascara2[palpite1 - 1] = simbolos[palpite1 - 1]
      mascara2[palpite2 - 1] = simbolos[palpite2 - 1]
      inicio = 0
      mascara = ''
      for numero in range (1, 2*nPares + 1):
        mascara += mascara2[inicio] + ' '
        inicio = inicio + 1
      print (montaTela(nPares))
      print (mascara)
      print ('')
    else:
      palpitesdados.remove(palpite1)
      time.sleep(1.5)
      print ('Que pena! Escolha errada. Os pares de símbolos ainda continuam assim:')
      print ('')
      print (montaTela(nPares))
      print (mascara)
      print ('')
    if '*' not in mascara:
      print ('Parabéns ' + nome + ', você ganhou o jogo da memória!')
      print ('')
      break    

#Então, eu consegui fazer o código do jogo e acredito que esteje uns 80% funcional, mas tenho dificuldade na parte da máscara e também não consegui modularizar tudo em funções como o exercício pede. Então, se puder ajudar, obrigado!!      
