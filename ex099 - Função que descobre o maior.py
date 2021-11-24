# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu
# programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* valores):
    print(f'Dos valores adicionados {valores}\nO maior entre eles foi {max(valores)}')


maior(6, 4, 3, 11, 2, 18)

