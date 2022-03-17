#desafio 9
#Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário com 15% de aumento

sat = float(input('Digite o salário atual:'))
aum = (15/100)*sat
nsa = sat+aum
print('Parabéns seu novo salário é de {} reais!'.format(nsa))