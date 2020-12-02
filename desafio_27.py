"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
"""

nome_completo = str(input('Digite o seu nome completo: '))

def lista_primeiro_ultimo_nome():
    nome_separado = nome_completo.strip().split()
    print(f'primeiro: {nome_separado[0]}')
    print(f'último: {nome_separado[-1]}')

lista_primeiro_ultimo_nome()