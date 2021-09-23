#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

nome = str(input("Digite seu nome\n"))
num = int(input("{}, qual tabuada você gostaria de saber ?".format(nome)))

print("{}, a tabuada desse número é\n {} X 1 = {}\n {} X 2 = {}\n {} X 3 = {}\n {} X 4 = {}\n {} X 5 = {}\n {} X 6 = {}\n {} X 7 = {}\n {} X 8 = {}\n {} X 9 = {}\n {} X 10 = {}".format(nome, num, num*1, num,num*2,num,num*3,num,num*4,num,num*5,num,num*6,num,num*7,num,num*8,num,num*9,num,num*10))
