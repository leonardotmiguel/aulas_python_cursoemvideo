'''
Desafio 13
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
'''

salario = float(input('Digite o seu salário atual: R$ '))
aumento = (salario * 15) / 100
novoSalario = salario + aumento

print(f'Seu novo salário com aumento de 15% é de R$ {novoSalario:.2f}')