"""
Dunder Main e Dunder Name

Dunder -> Dual Under -> Dois Underlines -> __

Ex: quando criamos um Python Package, dentro da pasta vem um __init__

Dunder Main -> __main__
Dunder Name -> __name__

Em Python são utilizados Dunder para criar funções, atributos/ propriedades e etc, utilizando __ para não gerar
conflito com os nomes desses elementos na programação.

# Na linguágem C temos a seguinte forma:

int main(){

    return 0;
}


# Em Java:

public static void main(String[] args{

}


- Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente o Python atribuirá a
variável __name__ o valor __main__ indicando que este módulo é o módulo de execução principal.

- Utilizaremos um módulo salvo qualquer para demonstrar a aplicação, para ver como funciona abro móduo utilizado.


OBS: Se for o módulo original: __name__ == '__main__', caso contrário: __name__ == '__<nome do modulo>__'
"""

from AAmodule_teste import _razao

print(_razao(2, 4))