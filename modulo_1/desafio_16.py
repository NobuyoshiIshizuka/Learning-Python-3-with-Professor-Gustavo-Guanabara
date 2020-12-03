"""
Quebrando um número
"""
from math import trunc
from math import floor
from math import ceil

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
class TruncNum:
    def __init__(self, num):
        self.num = num

    def devolve_num_truncado(self):
        return trunc(self.num)

    def devolve_num_acima(self):
        return ceil(self.num)

    def devolve_num_abaixo(self):
        return floor(self.num)


if __name__ == '__main__':
    num_trunc = TruncNum(float(input('Digite um número real: ')))

    #print(num_trunc.devolve_num_truncado())

    #print(num_trunc.devolve_num_acima())

    print(num_trunc.devolve_num_abaixo())
