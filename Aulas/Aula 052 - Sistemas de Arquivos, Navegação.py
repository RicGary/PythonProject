"""
Sistema de Navegação de Arquivos.

Para fazer a manipulação dos arq. do sistema precisamos importar o módulo "os".

os -> Operating System -> Sistema Operacional



# Verificar o diretório corrente
# Get current directory
print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir()
os.chdir('..')
print(os.getcwd())


# Podemos checar se um diretório é absoluto ou relativo
# Esta forma é apenas para o windows, e não sistemas posix

print(os.path.isabs('C:/Users/ericn/Documents/GitHub')) # True, é absoluto

"""

import os

print(os.getcwd())

os.path.join(os.getcwd(), 'Teste')
