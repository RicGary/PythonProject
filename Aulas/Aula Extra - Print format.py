"""
Algumas forma de formatar seu print.

print(1,2,3,4,sep=' | ')    # Separa com determinado valor.

print(1,2,3,4,'',end='')    # end = '' faz com que a frase termine com tal valor, por default \n.
print(5,6,7,8)

# Formas interessantes de usar o separador

print(1,2,3,4,5,6,sep='\n')     # Imprime em cada linha

# Utilizando o Format

yes_votes = 42_572_654
no_votes = 43_132_495
porcentagem = yes_votes / (yes_votes + no_votes)

print(f'{yes_votes} YES votes {porcentagem}')
print(f'{yes_votes:-9} YES votes {porcentagem:2.2%}')   # 9 espaços contando da direita para esquerda
                                                        # 2 algarismos antes e 2 depois da vírgula e converter
                                                        # Para porcentagem
s = 'Hello, World'
print(s)
print(repr(s))
"""

import math

print(f'O valor do pi é aproximadamente {math.pi:.3f}')     # Arredonda para 3 casas depois da vírgula

dic = dict(Eric = 98014, Rafael = 19378, Pricila = 13324)
for nome, celular in dic.items():
    print(f'{nome:10} ===> {celular:10d}')      # Usar : e depois um inteiro da espaçamento. Útil para alinhar.

print('-='*19)

for x in range(10):
    print(f'│{x:5}│{x+10:5}│{x+20:5}│{x+30:5}│{x+40:5}│{x+50:5}│')

print('-='*19)
