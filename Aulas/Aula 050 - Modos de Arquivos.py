"""
Modos de Arquivo

https://docs.python.org/3/library/functions.html#open

'r' = Abre para leitura -> padrão
'w' = Abre para escrita -> sobrescreve caso o arquivo já exista.
'x' = Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError.
'a' = Adiciona conteúdo ao FINAL do arquivo, SEMPRE.
'+' = Abre para atualização: Leitura e Escrita.

# Exemplo x

try:
    with open('zznao_existe.txt', 'x') as f:
        f.write('teste de conteudo')
except FileExistsError:
    print('Arquivo já existe')

with open('zznum.txt', 'a') as f:
    f.write('atualizando')
"""

with open('zznum.txt', 'a') as f:
    f.write('atualizando')