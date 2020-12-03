"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo um escolhido.
"""

from random import choice  #importando o método choice do pacote random

def lista_alunos():
    alunos = []
    for aluno in range(1,5):
        alunos.append(input(f'Insira o nome do {aluno}º aluno: '))
    return alunos

def escolhe_aluno():
    escolhido = choice(lista_alunos())
    return print(f'O aluno escolhido foi {escolhido}')

escolhe_aluno()
