#Melhore o jogo do Desafio 28 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, nostrando no final quantos palpites foram necessárias para vencer.

from random import randint
opcao = int
maquina = 0
t = 0   #tentativas

print('''\033[1;32mA máquina pensou em um valor entre 0 à 10.
Qual valor você acha que foi ?\033[m''')
while opcao != maquina:
    maquina = randint(0, 10)
    opcao = int(input('- '))
   #print(f'Você escolheu {opcao}\nMáquina: {maquina}')
    t = t + 1
print()     #pular uma linha.
print(f'Você finalmente acertou. Com um total de {t} tentativas.')
