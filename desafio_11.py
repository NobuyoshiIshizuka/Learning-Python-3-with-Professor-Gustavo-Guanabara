"""Faça um programa que leia a largura e a altura de uma parede em metros, calcula a sua área e a quantidade de tinta
    necessário para pintá-la, sabendo que cada litro de tinta, pinta um área de 2m²"""


class CalculoPinturaParede:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calculo_area(self):
        return self.largura * self.altura

    def calculo_tinta(self):
        return self.calculo_area() / 2

    def imprime_resultado(self):
        print(f'Você precisará de {self.calculo_tinta():.2f} latas de tintas para pintar uma area de'
              f' {self.calculo_area():.2f} M²')


if __name__ == '__main__':
    resultado = CalculoPinturaParede(float(input('Digite a altura da parede a ser pintada:')),
                                     float(input('Digite a largura da parede a ser pintada:')))

    resultado.imprime_resultado()
    
