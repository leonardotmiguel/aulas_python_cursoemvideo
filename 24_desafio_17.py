'''
Desafio 17
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa
'''

import math
co = float(input('Comprimnto do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca) # hypot importa o cálculo da hipotenusa
print(f'A hipotenusa vai medir {hi:.2f}')


'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')
# Resolução feita da forma matemática
'''