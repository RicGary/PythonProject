"""
Leitura de Arquivos

https://docs.python.org/3/library/functions.html#open

- Para ler o conteúdo de um arquivo e Python, utilizamos a função integrada .open()

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que neste caso
é o caminho para o arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos

OBS: Por padrão a função open() abre o arquivo para leitura, este arquivo deve existir ou então teremos o erro
FileNotFoundError

<_io.TextIOWrapper name='ztext_test.txt' mode='r' encoding='cp1252'>
<class '_io.TextIOWrapper'>

# UTF-8 -> é o encoding mais recomendável, pois ele lê caracteres especiais.

mode = 'r' -> modo de leitura <read>
encoding = 'cp1252' -> utilizado para ler carcteres
"""

arquivo = open('ztext_test.txt', encoding='utf-8')

# print(arquivo)
# print(type(arquivo))

# Para ler utilizamos a função read()

ret = arquivo.read()
print(type(ret))    # string
print(ret)

print(arquivo.read())
print(arquivo.read())

# OBS: O Python utiliza um recurso para trabalhar com arquivos chamado Cursor. Esse Cursor, funciona
# como o cursor quando estamos escrevendo.

#OBS**: A função read() lê todo o conteúdo do arquivo.

