#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considerando o dolar do dia 20/09/2021

nome = str(input("Digite seu nome "))
cart = float(input("{}, digite o valor que você tem na carteira ".format(nome)))

print("\n")
print("{}, você poderia comprar {:.2f} dólares em 2021\n".format(nome, cart/5.34))
print("Que merda, em {} ?!".format(nome))
