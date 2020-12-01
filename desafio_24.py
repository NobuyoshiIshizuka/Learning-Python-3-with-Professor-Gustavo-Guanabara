"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'
"""

nome_cidade = str(input('Digite o nome da cidade: ')).strip().upper()

def comparar_nome_cidade():
    convertendo = nome_cidade[0:5]
    if convertendo == 'SANTO':
        return True
    else:
        return False

print(comparar_nome_cidade())