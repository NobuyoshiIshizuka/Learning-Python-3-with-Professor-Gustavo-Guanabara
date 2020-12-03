"""
Converssor de Moedas
"""
# Desafio 10 Crie um converssor de Moedas de Real para Dollar
class ConverssorMoedas:
    def __init__(self, valor):
        self.valor = valor

    def moeda_convert(self):
        return self.valor / 5.34

    def imprime_valor(self):
        print(f'R${self.valor:.2f} é igual a ${self.moeda_convert():.2f} Dolar Americanos!')


if __name__ == '__main__':
    print('Valor atualizado dia 29/11/2020')
    resultado = ConverssorMoedas(float(input('Digite a quantidade em R$ que você deseja converter: ')))
    resultado.imprime_valor()


