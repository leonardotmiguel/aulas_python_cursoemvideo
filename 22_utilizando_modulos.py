'''
Explicação de como utilizar módulos em Python, utilizando os comandos import e from/import no Pytho.
'''

import math     # Importa o módulo 'math', que contém funções matemáticas prontas
num = int(input('Digite um número: '))

# Mostra a raiz quadrada arredondada para cima.
# 'math.ceil()' sempre arredonda para o próximo número inteiro, mesmo que já esteja muito próximo do inteiro anterior.
raiz = math.sqrt(num)   # Calcula a raiz quadrada inteira usando a função 'isqrt' do módulo 'math'
print(f'A raiz quadrada de {num} é {math.ceil(raiz)}')


'''
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz quadrada de {num} é {}.')
'''