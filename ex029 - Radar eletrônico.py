# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Digite a velocidade em Km/h: ' ))

if vel>=80.9:
    print('Você terá que pagar {} R$ de multa' .format((vel - 80) * 7))
else:
    print('Você ainda está dentro do limite de velocidade.')

