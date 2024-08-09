#28
from random import randint 
from time import sleep
pc = randint(0,5) #faz o computador sortear
n = str(input('Informe seu nome:'))
print('-=-' * 25)
print('Olá {}! Pensei em um número entre 0 e 5, tente adivinhar, se for capaz! '.format(n))
print('-=-' * 25)
jogador = int(input('Qual número eu pensei:'))
print('PROCESSANDO...')
sleep(4)
if jogador == pc:
    print('Parabéns infelizmente você acertou!')
else:
    print('Ganhei trouxa, o número que pensei foi {}'.format(pc))