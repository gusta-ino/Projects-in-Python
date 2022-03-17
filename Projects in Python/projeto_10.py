#desafio 4 
#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

m = float(input('Insira o valor em metros:'))

cm = (m/100)*10000

mm = (m/1000)*1000000

print('O valor em metros é {} \n Convertidos são: {}cm\n E {}mm' . format(m,cm,mm))