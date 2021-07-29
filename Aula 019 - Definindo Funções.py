"""
Definindo Funções

- Funções são pequenos trechos de código que realizam tarefas específicas.
- Pode ou não receber entrada de dados e retornar uma saída de dados.
- Muito úteis para executar procedimentos similares por repetidas vezes.

OBS: Se você possui uma função que faz várias tarefas dentro dela é bom
fazer uma verificação para que a função seja simplificada.

# Como usar:

def nome_da_funcao(dados, dados2):
    return list(dados,dados2)   # Return retorna um valor final

# Utilizando no dia a dia:

def diz_oi():
    print('Olá mundo')

diz_oi()

# OBS: A função só será executada caso você "Chame" ela.
# OBS: Só executa o que está dentro da tarefa, por exemplo, a função nome_da_funcao(dados, dados2)
# não foi executada pois não foi chamada.


# Usando a função com um retorno

def soma(lista):
    sm = sum(lista)
    listona = [1,2,325,32]
    blablabla = ['bla bla bla']

    return sm

print(soma([1,2,3,4,5]))
#print(listona)
#print(blablabla)

# No final "return" faz exatamente isso, retorna um valor selecionado dentro da função
# e não retorna outros, ele também finaliza a operação.

def lista(dados):

    if len(dados) == 0:
        return 0
    else:
        return sum(dados)

print(lista([]))
print(lista([1,2,3,4]))

# A função quebra o loop e encerra a função, ao mesmo tempo, retorna seu valor.

# OBS: podemos passar também uma função com um valor padrão.

def aniversario(nome = 'Eric', idade = '21'):
    print(f'Feliz Aniversário {nome}!Parabéns pelos seus {idade} anos!')

aniversario()
aniversario('Luiz','25')

# É sempre bom documentar uma função dizendo o que ela faz, por exemplo:

def fibbo(n):
    '''Calcula a sequência de Fibbonachi até 'n' lugar.'''
    dados = [1,1]
    for i in range(n):
        dados.append(dados[i]+dados[i+1])
    return dados

print(fibbo(5))
"""
