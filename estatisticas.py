"""Declaração de variáveis"""

time = list()
jogador = dict()
partidas = list()

"""Validação dos dados inseridos pelo usuário"""

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do Jogador: ')).title()
    tot = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    partidas.clear()
    for pj in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {pj+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? (S/N): ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

"""Programa principal"""

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'  -- Levantamento de Jogador {time[busca]['Nome']}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'     No jogo {i + 1} fez {g} gols.')
        print('-' * 40)
