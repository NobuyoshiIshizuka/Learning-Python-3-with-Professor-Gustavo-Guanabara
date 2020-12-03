"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado.
"""


def imprime_tracos():
    print(20 * '-')

def imprime_titulo():
    imprime_tracos()
    print('Locadora de Carros ')
    imprime_tracos()

def calculo_diaria_km(diaria, km):
    return (diaria * 60.00) + (km * 0.15)


imprime_titulo()
opcao = calculo_diaria_km(int(input('Digite a quantidade de dias que você ficou com o carro: ')),
                          float(input('Digite a quantidade de KM que você rodou com o carro: ')))
imprime_tracos()
print(f'O preço total do aluguel do carro ficou: R${opcao:.2f}')


