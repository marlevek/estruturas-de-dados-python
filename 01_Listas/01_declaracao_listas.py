frutas1 = ['laranja', 'abacate', 'morango', 'goiaba']
print(frutas1)
print(frutas1[1])
print(frutas1[-2])

frutas = []
print(frutas)

letras = list('python')
print(letras)

numeros = list(range(10))
print(numeros)

carro = ['ferrari', 'F50', 4200000, 2020, 2900, 'Curitiba', True]
print(carro)
print()
print('****** LISTA ANINHADA ******')

# lista aninhada (matriz)
matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

print(matriz)
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

print()
print('****** FATIAMENTO EM LISTAS ******')
print(matriz[0][1:2], '\n')
print(matriz[1:2], '\n')
print(matriz[:2], '\n')
print(matriz[::], '\n')

# iterando com for
carros = ['gol', 'celta', 'palio']
for carro in carros:
    print(carro)

# List Comprehension
nomes_carros = [carro for carro in carros]
print(nomes_carros)