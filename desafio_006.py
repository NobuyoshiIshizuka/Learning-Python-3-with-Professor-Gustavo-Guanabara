import math
"""
Crie um Algoritimo que leia um número inteiro e mostre o seu dobro, triplo e rais quandrada
"""

num = int(input("Digite um número para saber sua Raís quadrada, doblo e o seu triplo: "))

def rais_quadrada(num):
    return pow(num, 1/2)

def doblo(num):
    return num * 2

def triplo(num):
    return num * 3

def mostra_resultado():
    print('A rais quadrada de num é: ', rais_quadrada(num))
    print('O Doblo do número é: ', doblo(num))
    print('O triplo do valor é: ', triplo(num))


result = mostra_resultado()





