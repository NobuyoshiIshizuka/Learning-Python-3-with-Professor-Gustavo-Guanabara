"""
Desenvolva um programa que leia o comprimento de très retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da primeira reta: '))
r3 = float(input('Digite o comprimento da primeira reta: '))


if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r2 + r1:
    print('Os elementos podem formar um triângulo. ')
else:
    print('Os elementos não podem formar um triângulo.')



