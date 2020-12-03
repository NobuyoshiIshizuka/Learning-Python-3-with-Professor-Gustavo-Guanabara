"""
Crie um program que leia dois numeros e mostre a soma entre eles.
"""


class Soma:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma_valores(self):
        return self.num1 + self.num2

    def show_type(self):
        return type(self.num1)


if __name__ == '__main__':
    resultado = Soma(int(input("Entre com o primeiro número: ")),
                     int(input("Entre com o segundo Valor: "))).soma_valores()

    print(f'A soma entre os números é {resultado}')
    print(f'Os números digitados são do tipo {type(resultado)} ')








