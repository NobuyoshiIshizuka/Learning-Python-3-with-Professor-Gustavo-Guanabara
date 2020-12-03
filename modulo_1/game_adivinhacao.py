"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu
ou perdeu.
"""


import random
from time import sleep


class Adivinhacao:
    def __init__(self, numero):
        self.numero = numero

    def comparar_chute(self):
        num = random.randint(1, 5)
        if self.numero == num:
            criar_divisor()
            print(f'Parabéns você acertou! O número secreto era: {num}')
            criar_divisor()
        else:
            criar_divisor()
            print(f'Você errou! Tente novamente.')
            print(f'O número secreto era: {num}')
            criar_divisor()


if __name__ == '__main__':

    def criar_divisor():
        print('-=-' * 20)

    criar_divisor()
    chute_usuario = Adivinhacao(int(input('Tente adivinhar o número inteiro secreto: ')))
    criar_divisor()
    print('Processando...')
    sleep(2)
    chute_usuario.comparar_chute()

