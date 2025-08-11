'''
Desafio 14
Escreva um programa que converta uma temperatura digitada em C° e converta para F°
'''

temperatura = float(input('Digite a temperatura: '))
f = ((9 * temperatura) / 5) + 32
print(f'A temperatura de {temperatura}°C corresponde à {f}°F')
