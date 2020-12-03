"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva no Nome'
"""

nome = str(input("Digite um nome completo: ")).strip().title()

def compara_nome():
   return 'Silva' in nome

print(f'Seu nome têm silva? {compara_nome()}')