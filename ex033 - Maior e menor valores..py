#Faça um programa que leia 3 números e diga qual é menor e qual é o menor.

print('Digite aqui 3 valores: ')
n1 = int(input('- '))
n2 = int(input('- '))
n3 = int(input('- '))

lista = [n1, n2, n3]
ordem = sorted(lista)

print(f'''O maior valor é {ordem[2]}
O menor valor é {ordem[0]}''')
