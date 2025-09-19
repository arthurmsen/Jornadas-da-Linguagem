print ('Jogo do Campo minado')

import random

msg1 = input ('Digite o número de colunas desejado: ')
msg2 = input ('Digite o número de linhas desejado: ')
msg3 = input ('Digite o número de bombas desejado: ')

colunas = int (msg1)
linhas = int (msg2)
totalbombas = int (msg3)

posicaobombas = []
posicoesutilizadas = []
while True:
    x = random.randint (1, colunas)
    y = random.randint (1, linhas)
    for numero in range (totalbombas):
      if [x, y] not in posicoesutilizadas:
          posicaobombas.append([x, y])
          posicoesutilizadas.append([x, y])
    if len (posicaobombas) == totalbombas:
      break      
print ('')
print ('As posições das bombas são:')
print ('')
print (posicaobombas)
print ('')

posicoesdestaque = []
a1 = 0
contagem = 0
while contagem < len (posicaobombas):
  a2 = posicaobombas[a1][0]
  b2 = posicaobombas[a1][1]
  if a2 == 1:
    if b2 == 1:
      posicoesdestaque.append ([a2 + 1, b2])
      posicoesdestaque.append ([a2, b2 + 1])
    elif b2 != 1 and b2 != linhas:
      posicoesdestaque.append ([a2 + 1, b2])
      posicoesdestaque.append ([a2, b2 - 1])
      posicoesdestaque.append ([a2, b2 + 1])
    else:
      posicoesdestaque.append ([a2 + 1, b2])
      posicoesdestaque.append ([a2, b2 - 1])
  elif a2 != 1 and a2 != colunas:
    if b2 == 1:
      posicoesdestaque.append ([a2 + 1, b2])
      posicoesdestaque.append ([a2 - 1, b2])
      posicoesdestaque.append ([a2, b2 + 1])
    elif b2 != 1 and b2 != linhas:
      posicoesdestaque.append ([a2 + 1, b2])
      posicoesdestaque.append ([a2 - 1, b2])
      posicoesdestaque.append ([a2, b2 + 1])
      posicoesdestaque.append ([a2, b2 - 1])      
    else:
      posicoesdestaque.append ([a2 + 1, b2])
      posicoesdestaque.append ([a2 - 1, b2])
      posicoesdestaque.append ([a2, b2 - 1])
  else: 
    if b2 == 1:
      posicoesdestaque.append ([a2 - 1, b2])
      posicoesdestaque.append ([a2, b2 + 1])
    elif b2 != 1 and b2 != linhas:
      posicoesdestaque.append ([a2 - 1, b2])
      posicoesdestaque.append ([a2, b2 - 1])
      posicoesdestaque.append ([a2, b2 + 1])
    else:
      posicoesdestaque.append ([a2 - 1, b2])
      posicoesdestaque.append ([a2, b2 - 1])
  a1 = a1 + 1            
  contagem = contagem + 1

x = 1
y = 1
while y <= linhas:
  posicoes = []
  for elemento in range (colunas):
    if [x, y] not in posicaobombas:
      if [x, y] not in posicoesdestaque:
        posicoes.append ('-')
      else:
        if [x - 1, y] and [x + 1, y] in posicaobombas:
          if [x, y + 1] in posicaobombas:
            posicoes.append ('2')
          elif [x, y - 1] in posicaobombas:
            posicoes.append ('2')
          else:
            posicoes.append ('1')
        else:
          posicoes.append ('1')        
    else:
      posicoes.append ('*')      
    x = x + 1      
  linha = ''
  for i in range (len (posicoes)):
    linha = linha + posicoes[i]
  print (linha)
  x = 1
  y = y + 1
