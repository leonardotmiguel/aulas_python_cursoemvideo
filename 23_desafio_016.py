'''
Desafio 16
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
Exemplo: 
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
'''


import math

numero = float(input('Digite um número: '))
print(f'O valor digitado foi {numero} e sua porção inteira é {math.trunc(numero)}')
# Função trunc vai cortar a parte fracionário do número, deixando apenas a parte inteira.


'''
Outro método, usando apenas int

numero = float(input('Digite um número: '))
print(f'O valor digitado foi {numero} e sua porção inteira é {int(numero)}')
'''
