#desafio 023
#Faça um programa que leia um numero de 0 a 9999 e mostre
#na tela cada um dos  digitos separados

n = str(input('Digite um número de 0 a 9999:'))

print('Unidade ', n[3:4])
print('Dezena ', n[2:3])
print('Centena', n[1:2])
print('Milhar', n[0:1])
