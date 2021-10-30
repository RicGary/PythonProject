"""
Bloco With

O bloco with é utilizado para criar um contexto de trabalho, onde os recursos
utilizados são fechados após o bloco with.


# Com esse recurso aqui, chame ele de arquivo e trabalhe dentro do bloco.
# Após a saída o bloco será fechado automaticamente.
with open('ztext_test.txt', encoding='utf-8') as f:
    print(f.readlines())

"""
