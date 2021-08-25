from webbrowser import open
from threading import Timer
def Hello():
    open('https://www.youtube.com/watch?v=Yw6u6YkTgQ4&t')
t = Timer(5.0, Hello)
t.start()
"""
Nesta aula o objetivo é aprender o método input() e algumas formas de utilizar
o print()

print("Qual seu nome?")
nome = input()

# print('Bem-vindo %s' % (nome.title()))
idade = input('Qual sua idade?')

print(f'Bem vindo {nome}')

# print('Bem vindo {0} de {1}' .format(nome.title(), idade))

# print('Sinta-se à vontade %s de %s anos.' % (nome,idade))
"""
print('Hello World!')