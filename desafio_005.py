class SucessorAndAntecessor:
    def __init__(self, num1):
        self.num1 = num1

    def mostra_sucessor(self):
        return print(self.num1 +1)


    def mostra_antecessor(self):
        return print(self.num1 - 1)


if __name__ == '__main__':
    result = SucessorAndAntecessor(int(input('Digite um número para saber o sucessor e antecessor: ')))

    result.mostra_antecessor()
    result.mostra_s()
    

