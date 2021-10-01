#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Digite a distância da viagem: '))
if dist <= 200:
    print('Você vai pagar R${:.2f} nos seus {} Km percorridos' .format(dist * 0.5, dist))
else:
    print('Você vai pagar R${:.2f} nos seus {} Km percorridos' .format(dist * 0.45, dist))
