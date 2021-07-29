"""
Entendendo o * args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar
de qualquer coisa, desde que comece com asterisco "*".

Exemplo:

*xis

Mas por convenção a comunidade decidiu chamá-lo de *args para definí-lo.

Mas o que é o parâmetro *args?
- O *args utilizado em uma função coloca os valores extras informados como entrada
em uma tupla. Então desde já lembre-se que tuplas são imutáveis.


# Exemplo:

def soma_numeros(num1,num2,num3):
    return num1 + num2 + num3

# Se faltar um parâmetro, por exemplo coloca apenas num1 e num2, ocasionará em erro.
# Uma forma de corrigir este erro é:

def soma_numeros(num1,num2,num3=0):
    return num1 + num2 + num3

# Porém não é a forma mais correta.

# Entendendo o *args.

def soma_numeros(*args):
    print(args)

#soma_numeros()
#soma_numeros(1,2)
#soma_numeros(1,4,2)

# Utilizando ele.

def soma_numeros(*args):
    total = 0
    for num in args:
        total += num
    print(total)

soma_numeros()
soma_numeros(1,2)
soma_numeros(1,4,2)

# Ou também:

def soma_numeros(*args):
    total = sum(args)
    print(total)

soma_numeros()
soma_numeros(1,2)
soma_numeros(1,4,2)

# Não é obrigatório dar valor para o *args.

def lista(nome, email, *telefone):
    print(f'Bem-Vindo {nome}. Seu email {email} está lotado.Número cadastrado: {telefone}.')

lista('Eric Naiber','emailgenerico@gmail.com')
lista('Eric Naiber','emailgenerico@gmail.com','+55 51 980182736')

# O * mostra que estamos passando uma coleção de dados.
"""