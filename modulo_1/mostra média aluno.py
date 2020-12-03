class Media:
    def __init__(self, nota1, nota2, nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcula_nota(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3


if __name__ == '__main__':
    nota1 = float(input("Digite sua primeira Nota: "))
    nota2 = float(input("Degite a sua segunda Nota: "))
    nota3 = float(input("Digite a sua terceira Nota: "))

    result = Media(nota1, nota2, nota3).calcula_nota()
    print(f'A sua média foi {result}')

    if result > 7:
        print("Parabéns Você foi aprovado no curso")
    elif result < 7 and result >= 5:
        print("Você ficou de Recuperação")
    else:
        print("Você foi reprovado")

