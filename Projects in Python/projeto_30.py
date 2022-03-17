#Faça um programa que leia uma frase pelo teclado e mostre
#quantas vezes aparece a letra 'a'
#em que posição ela aparece a primeira vez
#em que posição ela aparece pela ultima vez

frase = str(input('Digite uma frase:')).lower().strip()
print('A letra "a" aparece {} vez(ez).'.format(frase.count('a')))
print('A primeira vez que a letra "a" apareceu na frase foi na posição {}'.format(frase.find('a')+1))
print('A ultimas vez que a letra "a" apareceu na frase foi na posição {}'.format(frase.rfind('a')+1))


