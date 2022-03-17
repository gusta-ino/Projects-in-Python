#desafio 8
#Faça um algoritimo que leia o valor de um produto e mostre seu novo preço, com 5% de desconto

vp = float(input('Insira o valor de produto:'))
vd = (5/100)*vp
vf = vp - vd 

print('O valor do produto com desconto é de {} reais' .format(vf))