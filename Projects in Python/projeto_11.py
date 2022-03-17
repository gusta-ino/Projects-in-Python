#desafio 5
# Faça um programa em que leia um número inteiro e mostre sua tabuada na tela

n = int(input('Digite um número:'))
print('A tabuada do {} é:'.format(n))
print('{0} x 1 = {1} \n{0} x 2 = {2} \n{0} x 3 = {3} \n{0} x 4 = {4} \n{0} x 5 = {5} \n{0} x 6 = {6} \n{0} x 7 = {7} \n{0} x 8 = {8} \n{0} x 9 = {9} \n{0} x 10 = {10}'  .format(n , (n * 1) , (n*2) , (n*3) , (n*4) , (n*5) , (n*6) , (n*7) , (n*8) , (n*9) , (n*10)))
