'''
Desafio 15
Escreva um programa que pergunte a quantdade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
'''
print('-' * 20)
print('LOCAÇÃO DE VEÍCULOS')
print('-' * 20)

dia = int(input('Digite quantos dias locados: '))
rodado = float(input('Digite quantos km rodados: '))
total = (dia * 60) + (rodado * 0.15)

print(f'O veículo ficou locado por {dia} dias.')
print(f'O veículos percorreu {rodado} km.')
print(f'O valor total é de R$ {total:.2f}')
