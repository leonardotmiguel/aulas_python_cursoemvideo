'''
Operações Aritméticas na Programação
+ adição
- subtração
* multiplicação
/ divisão
** potência
// divisão inteira
% resto de divisão
'''

'''
5+2 == 7
5-2 == 3
5*2 == 10
5/2 == 2.5
5**2 == 25
5//2 == 2
5%2 == 1
'''

'''
Ordem de Precedência
1 - ()
2 - **
3 - *, /, //, %
4 - +, -
'''

'''
Exemplo
5 + 3 * 2 == 11
3 * 5 + 4 ** 2 == 31
3 * (5+4) ** 2 == 243
'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma vale {s}, a multiplicação vale {m}, e a divisão vale {d}')
print(f'A divisão inteira vale {di} e a potência vale {e}')