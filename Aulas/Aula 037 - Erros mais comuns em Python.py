"""
Erros mais comuns em Python

A partir de agora teremos 5 aula, contando com essa, aprendendo a debugar o código e encontrar erros.

- Exemplo:

printf('Hello World!')

Traceback (most recent call last):
  File 'C:/Users/ericn/PycharmProjects/pythonProject/Aula 037 - Erros mais comuns em Python.py, line 8, in <module>
    printf('Hello World!')
NameError: name 'printf' is not defined

Traceback é a saida do erro.
    Está dizendo onde está o diretório do erro, na linha tal.
        printf('Hello World!') - Mostra o erro.
NameError: e um erro de nome.


• Erros mais comuns:

SyntaxError: Pyhton encontra um erro quando você escreve algo que ele não reconhece como parte da linguagem.
NameError: Quando um nome não foi definido. Erro de nome.
TypeError: Ocorre quando aplicamos uma função para um tipo errado. Por exemplo, não podemos fazer 5 + 'palavra'.
IndexError: Quando tenta acessar um elemento que não existe.
KeyError: Ocorre quando tentamos acessar um dicionário com uma chave inexistente.
IdentationError: Ocorre quando você esquece dos espaços dentro de um if/for/while etc.
AttributeError: Quando uma variável não tem atributo/função.
    - Exemplo:
        tupla = (4,3,2,1)
        tupla.sort()    Não existe sort() para tuplas, apenas em listas

ValueError: Ocorre qundo uma função ou operação built-in (integrada) recebe um argumento com tipo correto mas valor
inapropriado.
    - Exemplo:
        print(int('Eric'))      Não consegue converter esse tipo de string.

Você pode pesquisar 'datacamp python error list' na internet para encontrar outros tipos e expmeplos de erro.
"""
