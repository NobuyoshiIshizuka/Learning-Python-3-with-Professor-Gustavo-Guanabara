"""
Calculadora de descontos
"""


class Desconto:
    def __init__(self, valor, desconto):
        self.valor = valor
        self.desconto = desconto

    def calcular_desconto(self):
        return self.valor * (self.desconto / 100)

    def mostrar_desconto(self):
        print(f'O valor do desconto do produto é R${self.calcular_desconto():.2f}')


if __name__ == '__main__':
    resultado = Desconto(float(input('Digite o valor do Produto R$: ')),
                         float(input('Digite o valor do desconto em %: ')))

    resultado.mostrar_desconto()