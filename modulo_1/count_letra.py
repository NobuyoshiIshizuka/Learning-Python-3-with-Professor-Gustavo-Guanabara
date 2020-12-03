'''
Faça um programa que leia uma frase no teclado e mostre:
1 - Quantas vezes aparece a letra "A"
2 - Em que posição aparece ela a primeira vez.
3 - Em que posição ela aparece a última vez.
'''

frase = str(input('Digete uma frase: ')).strip().lower()

def quantos_A():
    return frase.count('a')

def primeiro_A():
    return frase.find('a',0,-1)

def ultimo_A():
    return frase.find('a',-1,0)

print(f'Sua frase têm {quantos_A()} a' )
print(f'Primeira aparição: {primeiro_A()}')
print(f'Ultima aparição: {ultimo_A()}')
