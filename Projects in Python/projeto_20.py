#desafio 017
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente'))
ca = ca**2
co = co**2
hip = math.sqrt(ca+co)

print('O valor da hipotenusa é {}' .format(hip))