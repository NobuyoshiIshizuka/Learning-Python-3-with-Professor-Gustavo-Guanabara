"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
foi multado. A multa vai custar R$7,00 por cada Km acima do limite
"""
velocidade = int(input("Digite a velocidade que o carro passou no radar: "))

def calcula_velocidade():
    if velocidade > 80:
        valor_multa = (velocidade - 80) * 7.00
        print('Você foi multado por passar acima de 80 Km/h, sua velocidade é: {}'.format(velocidade))
        print(f'Valor da multa é: {valor_multa}')
    else:
        print('Você é um bom motorista e respeita o limite de velocidade')

calcula_velocidade()