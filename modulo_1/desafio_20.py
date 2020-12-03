"""
Faça um programa que leia o nome de quatro alunos e mostre a ordem sorteada
"""


from random import shuffle
alunos = []
for aluno in range(1,5):
    alunos.append(input('Insira o nome do aluno: '))

shuffle(alunos)
print('A ordem de apresentação será: ')
print(alunos)



