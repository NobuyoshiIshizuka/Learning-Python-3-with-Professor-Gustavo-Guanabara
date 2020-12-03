"""
Converssor de metros para centimetros e milimetros
"""
class ConverssorDeMedidas:
    def __init__(self, metros):
        self.metros = metros

    def convert_centimetros(self):
        return self.metros * 100

    def convert_milimetros(self):
        return self.metros * 1000

    def mostra_valores(self):
        print(f'{self.metros} Metros convertido em milimetros é: ', self.convert_milimetros())
        print(f'{self.metros} Metros convertido em milimetros é: ', self.convert_centimetros())


if __name__ == '__main__':
    resultado = ConverssorDeMedidas(int(input("Digite a quantidade que você deseja converter: ")))

    print(resultado.mostra_valores())