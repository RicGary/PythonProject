'''
Níveis: * = Fácil, ** = Médio, *** = Difícil, **** = Muito Difícil
Evite utiizar def, import e loops já que o objetivo desta lista é aprimorar os conhecimentos sobre
os tipos: string, inteiro, booleano e float.

Ex.53 * :Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como
o preço do metro de tela.Imprima o custo para cercar este mesmo terreno com tela.

Ex.52 * :Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido pro-
porcionalmente ao valor que cada um deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um
ganharia do prêmio com base no valor investido.
                                                                          2
Ex.51 ** :Escreva um programa que leia as coordenadas x e y de pontos no R  e calcule
sua distância de origem (0,0), evite usar import math.

'''

#Ex.53: Resposta
'''
c, l = float(input('Comprimento do terreno:')), float(input('Largura do terrno'))
v = 10.50       #valor por metro do terreno
p = c + l       #perímetro
print(f'O valor para cercar o perímetro é de:{round(p*v,2)}R$')
'''
#Ex.52: Resposta
'''
Jorge = float(input('Valor do investimento de Jorge'))
Paulo = float(input('Valor do investimento de Paulo'))
Eric = float(input('Valor do investimento de Eric'))

Total = Jorge+Paulo+Eric
Porcentagem_Jorge = Jorge/Total
Porcentagem_Paulo = Paulo/Total
Porcentagem_Eric = Eric/Total

Loteria = 1e9  #1e9 = 1.000.000.000 ou seja 1 vezes 10 elevado na nove ou 1*10**9

Ganhou_Jorge = Porcentagem_Jorge*Loteria
Ganhou_Paulo = Porcentagem_Paulo*Loteria
Ganhou_Eric = Porcentagem_Eric*Loteria

print(f'Jorge ganhou {round(Ganhou_Jorge,2)}R$, Paulo ganhou {round(Ganhou_Paulo,2)}R$ e Eric ganhou {round(Ganhou_Eric,2)}R$.')
'''
#Ex.51: Resposta
'''
x = float(input('Coordenada de x: '))
y = float(input('Coordenada de y: '))

pitagoras = x**2+y**2
pitagoras = pitagoras**0.5      #o truque está aqui, lembre que raiz quadrada é definida por 1/2, cúbica 1/3...

print(f'A distância do ponto {x},{y} até o ponto de otigem é {round(pitagoras,3)}')
'''
#Os outros exercícios da lista seguem o mesmo padrão de dificuldade, parabéns por ter chegado até aqui.
#Mais exercícios ou códigos em https://github.com/RicGary