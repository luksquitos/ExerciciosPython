#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Qual será o primeiro termo da P.A ? '))
razao = int(input('Qual será a razão ? '))

for c in range(primeiro, primeiro + razao*11 - razao, razao):
    print(c)
