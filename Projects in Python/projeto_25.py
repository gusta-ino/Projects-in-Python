# Aula 09 - manipulando texto
frase = "Eu preciso tomar cafe hoje"
print(frase[2:10])
print(frase[2::2])
print(frase[:2])
print(len(frase))
print(frase.count('i'))
print(frase.count('i', 0, 15))
print(frase.find('iso'))
print(frase.find('casa'))
print('eu' in frase)
print(frase.replace('cafe', 'agua'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(frase.split())
print('-'.join(frase))



