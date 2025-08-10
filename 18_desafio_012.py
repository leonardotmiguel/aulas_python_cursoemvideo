'''
Desafio 12
Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
'''

preco = float(input('Digite o preço do produto: R$ '))
desconto = (preco * 5) / 100
novopreco = preco - desconto

print(f'O produto que custa R$ {preco}, com 5% de desconto passará a custar R$ {novopreco}')