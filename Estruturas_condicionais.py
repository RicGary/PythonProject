"""
Estudo de condicionais
if, else, elif
and, or:binários

not, is:uniários
"""

ativo = True
logado = True

if ativo and logado:            #Os dois precisam ser True para rodar
    print('Bem-vindo usuário.')

if ativo or logado:             #Apenas 1 precisa ser True
    print('Bem-vindo.')

if not aivo:                    #not inverte os valores True->False
    print('Você precisa ativar sua conta.')