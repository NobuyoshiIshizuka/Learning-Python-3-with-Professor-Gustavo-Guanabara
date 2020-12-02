"""
Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar
"""
def par_impar(num):
    if num % 2 == 0:
        print(f'{num} é um número par.')
    else:
        print(f'{num} é um número impar.')

par_impar(int(input('Digite um número inteiro para saber se ele é par ou impar: ')))