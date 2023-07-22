# Criação de tuplas
tupla = ()
print(type(tupla))

letras = tuple('Python')
print(letras, type(letras))
print(letras[3])

tpl_2 = (6, 8, 'a')
print(tpl_2, type(tpl_2))

# Métodos de tuplas
print(tpl_2.count(6))

print(tpl_2.index('a'))

pais = ('Brasil', )  # com vírgula no final
pais_b = ('Brasil')  # sem vírgula no final
print(type(pais), type(pais_b))
print()

print('TUPLAS ANINHADAS')
# Com isso pode-se criar tabelas e acessar informando os índices de linha e coluna

matriz = (
    (1, 'a', 2),
    ('b', 3, 4),
    (5, 6, 'c')
)
print(matriz)
print(matriz[0])
print(matriz[0][0])
print(matriz[:][2])

# Função enumerate
carros = ('gol', 'corsa', 'palio')
for indice, carro in enumerate(carros):
    print(indice, '-', carro)