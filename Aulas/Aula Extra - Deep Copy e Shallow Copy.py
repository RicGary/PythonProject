"""
Diferenças entre Deep Copy e Shallow Copy.

# Deep Copy ou Cópia Profunda

# Ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista
# mas elas ficaram totalmente independentes, ou seja, modificar uma lista não
# afeta a outra, isso em Python é chamado de Deep Copy ou Cópia Profunda.

lista = [1, 2, 3]
print('Lista:', lista)

nova = lista.copy()     # Cópia
print('Nova:',nova)

nova.append(4)

print('Lista:', lista)
print('Nova:',nova)


# Shallow Copy ou Cópia Rasa

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista
# para a nova lista, mas após realizarmos modificação em uma das listas essa
# modificação se refletiu em ambas as listas, isso em Python é chamado de
# Shallow Copy ou Cópia Rasa.

lista = [1,2,3]
print('Lista:', lista)

nova = lista        # Cópia
print('Nova:',nova)

nova.append(4)

print('Lista:', lista)
print('Nova:',nova)
"""