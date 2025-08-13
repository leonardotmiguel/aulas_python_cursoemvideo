'''
Desafio 20
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print('A ordem para apresentar o trabalho será: ')
print(lista)

'''
A função random.shuffle() em Python embaralha os elementos de uma lista in-place, ou seja, modifica a lista original diretamente, sem retornar uma nova lista. 

Para usar a função, você precisa importar o módulo random e, em seguida, chamar random.shuffle() com a lista que deseja embaralhar como argumento
'''