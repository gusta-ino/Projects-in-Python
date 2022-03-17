#desafio 6
#Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dolares ela pode comprar
#Considere $1 = R$ 3.27 

real = float(input('Quantos reais você possui?'))
print('Você pode comprar {0} dólares com {1} reais' .format(real/5.08 , real))