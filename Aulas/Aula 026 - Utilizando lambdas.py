"""
Utilizando lambdas.

Conhecidas por Expressões Lambdas, ou Funções Lambdas, são funções sem nome, ou seja,
funções anônimas.

# Função Python

def funcao(x):
    return 3 * x + 1
print('Função Python: ',funcao(4))

# Expressão Lambda
lambda x: 3 * x + 1

# Como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1      # Essa não é a melhor forma de utilizá-la.
print('Expressão Lambda: ',calc(4))

# Podemos ter expressões lambdas com múltiplas entradas (parâmetros).

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('     eric ','      naiber'))                               # .strip() retira espaço no início
print(nome_completo('ric  ',' GARY   '))                                        # e no fim da palavra.

# Em Funções Python podemos ter muitas entradas ou nenhuma. Em Lambdas também;

amar = lambda : 'Como não amar Python?'     # Nenhuma entrada
tres = lambda a, b, c: a+b+c                # Três entradas
print(
    amar(),
    tres(1, 1, 2),
    sep='\n'
)

# Se colocarmos mais valores do que o esperado, teremos TypeError.

# Outro Exemplo

autores = ['Machado de Assis', 'H. G. Wells', 'Pedro Salomão','Isaac Asimov', 'Clarice Lispector', 'Rupi Kauer']
# Parâmetro key= 'Por qual chave você quer fazer a ordenação?'
print(autores)
autores.sort(key = lambda sobrenome : sobrenome.split(' ')[-1].lower())

print(autores)
# Com o lambda ele quebra a palavra onde tem espaço e pega a última palavra ([-1]) colocando-a toda em minúsculo.

print('Machado de Assis'.split(' '))
print('Machado de Assis'.split(' ')[-1])
print('Machado de Assis'.split(' ')[-1].lower())


"""

# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Função Python
def funcao_quadratica(a,b,c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c """
    return lambda x : a * x ** 2 + b * x + c

teste = funcao_quadratica(2, 3, -5) # Valores da função quadrática (a, b, c)
print(teste(0))
print(teste(1))     # Valores de Lambda
print(teste(2))
