"""
Seek e Cursor

seek() -> Utilizada para mover o cursor.


arquivo = open('ztext_test.txt', encoding='utf-8')
print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)     # Move o cursor para o início

print(arquivo.read())


arquivo = open('ztext_test.txt', encoding='utf-8')

# print(arquivo.readline())   # Lê o arquivo linha a linha.

ret = arquivo.readline().split(' ')
print(ret)


arquivo = open('ztext_test.txt', encoding='utf-8')

linhas = arquivo.readlines()      # Lê todas as linhas, colocando cada linha em uma lista.

# OBS: Quando utilizamos open() é criado uma conexão do disco com seu computador, que é chamada de streaming.
# Ao finalizarmos essa conexão utilisamos close()


Passos para se trabalhar com arquivo.

Passo 1 - Abrir o arquivo.
f = open('ztext_test.txt', encoding='utf-8')

Passo 2 - Trabalhar o arquivo.
print(f.read())
print(f.closed)      # Verifica se está aberto.

Passo 3 - Fechar o arquivo.
f.close()

"""







