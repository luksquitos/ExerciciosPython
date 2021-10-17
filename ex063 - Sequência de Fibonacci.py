# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

valor = int(input('até onde você quer saber a sequencia de fibonacci? '))
soma = 1
anterior = 0
sucessor = 0
contador = 0
while valor != contador:
    print(soma, end='- ')
    sucessor = soma
    soma = sucessor + anterior
    anterior = sucessor
    contador += 1
