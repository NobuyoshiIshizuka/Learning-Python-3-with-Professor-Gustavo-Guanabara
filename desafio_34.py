"""
Escreva um programa que receba um salário de um funcionário e calcule o valor do aumento.
Para salários superiores a R$1250.00, calcule um aumento de 10%.
Para os salários inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Digite o salario: R$'))

def calcular_salario(salario):
    if salario > 1250.00:
        print(f'O salário após o aumento de 10% é:R${salario * 110 / 100}')
    elif salario <= 1250.00:
        print(f'O salário após o aumento de 15% é: R${salario * 115 / 100}')

calcular_salario(salario)
