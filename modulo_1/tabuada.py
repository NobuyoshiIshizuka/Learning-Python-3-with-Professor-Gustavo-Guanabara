class Tabuada:
    def __init__(self, num):
        self.num = num


    def mostra_tabuada(self):
        for i in range(1, 11):
            if i < 10:
                print(f'{self.num} X  {i} =  {self.num * i}')
            else:
                print(f'{self.num} X {i} = {self.num * i}')



if __name__ == '__main__':
    resultado = Tabuada(int(input("Digite o número que deseja ver a tabuada: ")))

    resultado.mostra_tabuada()