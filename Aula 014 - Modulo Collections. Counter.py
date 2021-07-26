"""
Módulo Collections - Counter

Collections -> High-performance Container Datetypes

Link para mais info.: https://docs.python.org/3/library/collections.html?highlight=collections#collections.Counter

Counter: Recebe um iterável como parâmetro e cria um objeto do tipo
Collenctions Counter que é parecido com um dicionário, contendo como
chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.


# Realizando o import

from collections import Counter

# Exemplo 1

# Poderia ser qualquer iterável, tupla, dicionário, string, etc...
lista = [1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7]

# Utilizando o Counter
res = Counter(lista)
print(res)
print(type(res))

# Para cada elemento da lista criou uma chave e colocou o valor como a quantidade
# de ocorrências.

# Exemplo 2

print(Counter('Eric Naiber'))
"""

# Realizando o import

from collections import Counter

# Exemplo 3 - Mais importante

texto = """
Python é uma linguagem de programação criada pelo holandês Guido Van Rossum, em 1991.
É reconhecida por ser muito versátil, com ênfase na legibilidade do código, e por ter 
uma abordagem que permite aos programadores desenvolverem algoritmos melhor estruturados.

Ela é orientada por uma lista de 19 princípios chamada de "The Zen of Python". Alguns deles são:

Bonito é melhor do que feio
Explícito é melhor do que subentendido
Simples é melhor do que complexo
Legibilidade é importante.
Por conta dessas características, a linguagem Python se tornou uma das preferidas dos programadores.
De acordo com o ranking TIOBE, que indica a popularidade das linguagens de programação, Python é 
a terceira mais utilizada pelos desenvolvedores.

Por que aprender Python vai impulsionar a sua carreira?
Aprender a programar é um diferencial que pode alavancar qualquer carreira. Isso porque a informatização
 abrange cada vez mais áreas, e profissionais capacitados para simplificar e digitalizar processos têm
  grandes vantagens sobre aqueles que não têm noções de programação.

E por que aprender Python, especificamente? Porque Python é uma das linguagens de programação mais fáceis
 e versáteis. Apesar de ser simples, você pode executar projetos de todos os tamanhos com ela.

Por isso, se você quer começar a programar em Python, saiba que é a linguagem ideal. E se você é um
 programador e quer aprofundar seus conhecimentos, saber Python é fundamental.
"""

palavras = texto.split()

#print(palavras)

res = Counter(palavras)
#print(res)

# Queremos saber quais palavras mais utilizadas (5 mais comuns).
print(res.most_common(5))
