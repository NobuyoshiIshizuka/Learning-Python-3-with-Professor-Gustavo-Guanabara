"""
Dissecando uma variável
"""


def dissecando_var(variavel):
    print(f'O tipo primitivo desse valor é {type(variavel)}')
    print('Só tem espaços? ', variavel.isspace())
    print('É um número? ', variavel.isnumeric())
    print('È um alfabeto?, ', variavel.isalpha())
    print('É um alfanumérico? ', variavel.isalnum())
    print('É maiuscula? ', variavel.isupper())
    print('É minuscula? ', variavel.islower())
    print('Está capitalizada? ', variavel.capitalize())


variavel = dissecando_var(input("Digite qualquer valor: "))

