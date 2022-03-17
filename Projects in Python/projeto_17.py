#exe 08
#Utilizando modulos(imports)

#duas formas de se importar uma biblioteca    
#import math
from math import sqrt
num = int(input('Digite um número:'))
#raiz = math.sqrt(num)
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}!' .format(num,raiz))