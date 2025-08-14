'''
O professor apresenta diversos conceitos essenciais para manipular strings (cadeias de texto) em Python, começando pelas operações básicas até métodos indispensáveis para qualquer desenvolvedor iniciante. Veja os pontos principais:

1. Fatiamento de String (String Slicing)
Você aprende como acessar pedaços de texto dentro de uma string usando a sintaxe string[inicio:fim:passo].
Exemplos típicos:
texto[0]: primeiro caractere.
texto[1:4]: caracteres do índice 1 ao 3, (o Python lê um caractere a menos do que foi pedido).
texto[:5]: primeiros cinco caracteres (sem um número antes do : ele considera do 0 em diante)
texto[5:]: do índice 5 até o fim (sem um número após o : ele considera do índice 5 até o fim)
texto[::2]: pulando de dois em dois, por exemplo.
texto[4::3]: ele vai iniciar, como não tem o número de fim, ele vai até o final, pulando de 3 em 3).


2. Análise de Texto com len()
A função len(texto) retorna o número total de caracteres da string, inclusive espaços e símbolos.


3. Método count()
Permite contar quantas vezes um trecho aparece dentro da string.
Exemplo: texto.count('a') informa o número de vezes que a letra "a" aparece na str.


4. Localização de Substrings: find() e rfind()
find(sub) retorna o índice da primeira ocorrência de sub ou -1 se não for encontrado.
rfind(sub) mesma situação do anterior, mas dá última para o início.
Úteis para identificar posições de palavras ou caracteres dentro de um texto.


5. Checar Conteúdo com in e not in
Podemos verificar se uma substring está presente ou ausente:
'py' in texto → True se "py" existir.
'x' not in texto → True se "x" não estiver lá.


6. Transformações de Maiúsculas e Minúsculas
lower(): converte toda a string para minúsculas.
upper(): converte toda a string para maiúsculas.
capitalize(): deixa apenas a primeira letra em maiúscula e o restante em minúsculas.
title(): coloca cada palavra com a primeira letra maiúscula.


7. Remoção de Espaços com strip(), lstrip(), rstrip()
strip(): remove espaços no início e no fim.
lstrip(): remove do início.
rstrip(): remove do fim.


8. Substituição de Texto com replace()
texto.replace("antigo", "novo") substitui todas as ocorrências de "antigo" por "novo" dentro da string.


9. Divisão e Junção com split() e join()
split(sep): divide a string em lista de palavras ou pedaços, com base em um separador (por padrão, espaço).
join(lista): combina uma lista de strings em uma única string, usando o separador que você escolher:
" ".join(lista) junta com espaços.
"-".join(lista) junta com hífens, por exemplo.
'''
