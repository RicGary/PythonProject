"""
StringIO

ATENÇÃO: para ler ou escrever dados em arquivos do sistema operacional, o software precisa ter permissão.
    - Permissão de leitura
    - Permissão de escrita

StringIO -> Utilizado para ler e criar arquivos em memória.
"""

# Primeiro fazemos o import

from io import StringIO

msg = 'Esta é apenas uma string padrão.'

# Podemos criar um arquivo em memória já com uma string inserida, ou mesmo vazio para inserirmos texto depois.
arq = StringIO(msg)
# arq = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos.

print(arq.read())
# Arquivo está na memória, e não no disco

