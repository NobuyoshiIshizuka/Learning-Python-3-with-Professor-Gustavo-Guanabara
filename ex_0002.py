"""
Comando Input
"""

# Desafio receba o nome do usuário guarde em uma variável e depois mostre na tela uma mensagem de boas vindas.

class Saudacao:
    def __init__(self, nome):
        self.nome = nome

    def msg_usuario(self):
        print(f'Olá {self.nome}, seja bem vindo ao curso de Python')

if __name__ == '__main__':
    usuario = Saudacao(input("Digite o seu Nome: ")).msg_usuario()