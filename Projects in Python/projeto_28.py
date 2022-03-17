#desafio 024
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

city = str(input('Digite o nome da cidade:'))
city1 = city.split()
print('santo' in city1[0])
