#desafio 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno do consseno e da tangente desse ângulo

import math
ang = float(input('Insira o ângulo:'))

cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O valor do seno é {:.2f}, do cosseno é {:.2f} e da tangente é {:.2f}'.format(sen,cos,tan))
