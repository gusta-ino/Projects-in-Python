#desafio 7
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a
#quantidade de tinta necessaria para pintá - la, sabendo que cada litro de tinta pinta uma area de 2m².

alt = float(input('Digite a altura em metros:'))
larg = float(input('Digite a largura em metros:'))
mq = alt*larg
ml = mq/2

print('A área de sua parede é {0} m² e a quantidade de tinta necessaria para pintá-la é de {1} litro(s) ' .format(mq , ml))