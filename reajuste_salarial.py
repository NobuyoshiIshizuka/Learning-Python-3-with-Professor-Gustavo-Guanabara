"""
Crie um programa que seja capaz de receber um salário e calcular o aumento deste.
"""
class ReajusteSalario:
    def __init__(self, salario, aumento):
        self.salario = salario
        self.aumento = aumento

    def calcular_porcentagem(self):
        return self.aumento + 100

    def aumentar_salario(self):
        return self.salario * self.calcular_porcentagem() / 100


if __name__ == '__main__':
    salario_atual = ReajusteSalario(float(input("Digite o salário: ")),
                                    float(input("Digite a porcentagem do aumento do salário: ")))

    print(salario_atual.aumentar_salario())
