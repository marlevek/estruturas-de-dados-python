lista = []

lista.append(1)
lista.append('Python')
lista.append([40, 20, 10])
print(lista)

print(lista.clear())
print(lista)

lista = [1, 'Python', [40, 20, 10]]
lista_copia = lista.copy()
print(lista_copia)

# mostrando que a lista e sua cópia são diferentes, por isso o que é feito na cópia não reflete na lista original
print(id(lista), id(lista_copia))

lista_copia.insert(2, 0)
print(lista_copia)

lista_copia.pop()
print(lista_copia)

linguagens = ['Python', 'Js', 'C++']
linguagens.extend(['Java', 'PHP'])
print(linguagens)

print(linguagens.index('Js'))

linguagens.reverse()
print(linguagens)

num = [2, 4, 5, 6, 2, 2]
print(num.count(2))

num.pop(5)
print(num)

num.remove(5)
print(num)

# Método sort
numeros = [8, 0, -3, 5]
print(numeros)
print(sorted(numeros))

numeros.sort(reverse=True)
print(numeros)

linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)


numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(numeros)