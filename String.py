"""

Estudo de strings.
'nome',  "nome",   ""nome""

"""

print('Eric \nNaiber')  # \n pula para próxima linha

print('Maria \' Eduarda')  # caracter de escape, \ faz printar o caracter à força

print('Eric é um cara legal'.split())  # transforma em uma lista com as palavras

print('Alo alo pessoal'.split('o'))  # retira 'o' e separa

# na verdade toda string é uma lista de caracteres, exemplo
nome = 'Eric otaku'
# ['E', 'r', 'i', 'c', ' ', 'o', 't', 'a', 'k', 'u']
#  0    1    2    3    4    5    6    7    8    9
# então podemos printar apenas uma parte
print(nome[0:4])  # do zero até o 4, porém 4 sai fora

print(nome.split()[0])  # faz split na palavra inteira, posição 0
print(nome.split()[1])

print(nome[::-1])  # vá do primeiro elemento até o último e inverta
