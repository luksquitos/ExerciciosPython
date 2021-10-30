# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = (
'Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino', 'International', 'Corinthians', 'Fluminense',
'Atlético-GO', 'América-MG', 'Cuiabá', 'Athletico-PR', 'São Paulo', 'Ceará', 'Bahia', 'Santos', 'Juventude', 'Sport',
'Grêmio', 'Chapecoense')

print(f'Os 5 primeiros times são {times[0:5]}')
print(f'Os ultimos 4 colocados são {times[-1:-5:-1]}')
print(f'Os times em ordem alfabética são {sorted(times)}')
print(f'Chapecoense se encontra na posição {times.index("Chapecoense") + 1}')
