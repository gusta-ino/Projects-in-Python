#desafio 11
#Crie um programa em que leia um número Real qualquer pelo teclado e mostre sua porção inteira

import math
n = float(input('Digite um númeor qualquer:'))
np = math.trunc(n)
print('O número {0} tem a parte inteira {1} '.format(n,np))