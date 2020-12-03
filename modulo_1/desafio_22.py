"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
1 O nome com todas as letras maiúsculoas e minúsculas
2 Quantas letras ao todo (sem considerar espaços).
3 Quantas letras têm o primeiro nome
"""


nome = str(input('Digite o seu nome completo: '))


def letras_maiusculas():
    return nome.upper()


def letras_minusculas():
    return nome.lower()


def contando_letras():
    contador = 0

    for letra in nome:
        if letra != ' ':
            contador += 1
    return contador


def primeiro_nome():
   nome_alterado = nome.strip().split()
   p_nome = nome_alterado[0]
   print(p_nome)
   print(len(p_nome))


print(letras_maiusculas())
print(letras_minusculas())
print(f'Seu nome inteiro têm: {contando_letras()}')
primeiro_nome()
