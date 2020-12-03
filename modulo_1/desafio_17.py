"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triângulo retuangulo,
calcule e mostre o cumprimento da hipotenusa
"""
from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
# hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
hipotenusa = hypot(co, ca)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')