"""
Desenvolva um programa que que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem cobrando R$ 0,50 por KM rodado até 200 KM e R$0,45 para viagens mais longas.
"""
preco = 0.0

def calcular_preco_passagem(distancia):
    if distancia <= 200 and distancia > 0:
        preco = distancia * 0.50
        print(f'O valor da viagem vai custar R${preco}')
    elif distancia > 200:
        preco = distancia * 0.45
        print(f'O valor da viagem vai custar R${preco}')
    else:
        print('A distância precisa ser maior do que 0')

resultado = calcular_preco_passagem(int(input('Digite a distância em KM: ')))

