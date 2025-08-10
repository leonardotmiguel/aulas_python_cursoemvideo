'''
Desafio 10
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere US$ 1,00 = R$ 3,27
'''

real = float(input('Quanto você tem de dinheiro? R$ '))
print(f'Se você tem R$ {real} na carteira, você poderá comprar {real/3.27} dólares')