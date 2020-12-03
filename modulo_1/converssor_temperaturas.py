"""
Converssor de temperaturas
"""
class ConverssorTemperaturas:
    def __init__(self, temperatura, conversao):
        self.temperatura = temperatura
        self.conversao = conversao

    def escolher_converssao_temp(self):
        if self.conversao == 'c' or self.conversao == 'C':
            return print(f'{(self.temperatura - 32) * 5/9} Cº')
        elif self.conversao == 'f' or self.conversao == 'F':
            return print(f'{(self.temperatura * 9/5) + 32} Fº')
        else:
            print('Você digitou um caracter inexistente digite "C" para celsius ou "F" para Farenheit')


if __name__ == '__main__':
    temp_atual = ConverssorTemperaturas(float(input("Digite a temperatura a ser convertida: ")),
                                        input("Digite 'C' para converter para celsius ou 'F' para Farenheit: "))

    temp_atual.escolher_converssao_temp()

