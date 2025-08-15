'''
Desafio 22
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome
'''

nome = 'Leonardo Teixeira Miguel'
print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ", "")))
print(len(nome.split()[0]))


'''
O método replace de strings cria uma nova string trocando um texto por outro.
parte_antiga → o que você quer substituir.
parte_nova → o que vai entrar no lugar.
" " - espaço (o que queremos remover)
"" - string vazia (nada para colocar no lugar)
Então nome.replace(" ", "") remove todos os espaços do nome.

Por que tem dois conjuntos de aspas duplas dentro dos parênteses
O replace recebe dois argumentos:
" " → primeiro argumento (o que será substituído)
"" → segundo argumento (com o que será substituído)
Eles estão entre aspas porque são strings.
O primeiro tem um espaço dentro → " "
O segundo está vazio → "" (string vazia significa “nada”).
'''