#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = str(input("Primeiro nome: "))
n2 = str(input("Segundo nome: "))
n3 = str(input("Terceiro nome: "))
n4 = str(input("Quarto nome: "))
list = [n1, n2, n3, n4]

print("A ordem escolhida foi \n", random.sample(list, 4))

# * Tive problemas com esse. A função que o Guanabara usou foi random.shuffle, mas eu não entendi como essa função
#não podia ser usada na função print.

