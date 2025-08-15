'''
Desafio 26
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "a"
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
'''

frase = 'Hoje foi um belo dia, o clima estava muito agradavel'
print('A letra "a" aparece', frase.count('a'),'vezes')
print('A primeira ocorrência acontece na posição', frase.find('a'))
print('A última ocorrência acontece na posição', frase.rfind('a'))