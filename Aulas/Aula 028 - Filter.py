"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Dados coletados de algum sensor.
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando média dos dados utilizando mean()
media = st.mean(dados)
print(media)

# OBS: Assim como a função map(), o filter() recebe dois parâmetros, sendo uma função
# e um iterável.

res = filter(lambda i: i > media, dados)
print(list(res))

# OBS: Assim como a função map(), após serem utilizados os dados de filter() são excluídos da memória.

paises = ['Brasil', 'Argentina', 'USA', 'Porto Rico', '', '', 'Colômbia']

res = filter(None, paises)  # Remove os espaços vazios
print(list(res))

# filter -> Recebe dois parâmetros e retorna um objeto, filtrando apenas os elementos de acordo com a função.

# Exemplo mais complexo

usuarios = [
    dict(username='samuel', tweets=['Eu adoro bolos', 'Eu adoro pizzas.']),
    dict(username='carla', tweets=['Eu adoro gatos.']),
    dict(username='bob123', tweets=['Fora Bolsonaro!']),
    dict(username='dogo', tweets=['Auauau']),
    dict(username='gal', tweets=[]),
    dict(username='jeff', tweets=[]),
    dict(username='ellon_musk', tweets=['Bitcoin não vale nada!', 'Comprem bitcoin vale muito!'])
]

# Filtrar usuários inativos no Twitter

inativos = list(filter(lambda u : len(u['tweets']) == 0, usuarios ))

print(inativos)
"""
import statistics as st
import webbrowser
from threading import Timer

# Combinar filter() com map()

nomes = ['Erica', 'Giovanne Giorgio', 'Paola', 'Michael']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que o nome tenha menos de 5 carcteres.

lista = list(map(lambda nome: f'Sua instrutora é a {nome}', filter(lambda nome: len(nome) <= 5, nomes)))
#print(lista)

# Devemos printar o apenas as pessoas com sobrenome, porém abreviando utilizando o segundo nome

lista = map(lambda nome: f'My name is {nome}, but everybody calls me {nome.split(" ")[1]}',
        filter(lambda nome: len(nome.split(' ')) > 1, nomes))
print(list(lista))

def giorgio():
    webbrowser.open('https://www.youtube.com/watch?v=QVzr_DJUoOs')

t = Timer(5.0, giorgio)
t.start()