'''
Desafio 11
Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
'''

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
metro = largura * altura
tinta = metro / 2


print(f'A sua parede tem {metro}m² de área e precisará de {tinta} litros de tinta para pintá-la. ')