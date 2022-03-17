#Diferentes operadores aritimeticos, quebra de linha e continuação de linha
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
soma = n1+n2
sub = n1-n2
multi = n1*n2
divi = n1/n2
diviex = n1//n2
elev = n1**n2
print('o valor da soma é igual a {}, \n Da subtração {}, \n Da multiplicação {},' .format(soma,sub,multi), end='')
print(' \n Da divisão {}, \n Da divisão exata {} \n E da exponenciação {} respectivamente'.format(divi,diviex,elev))