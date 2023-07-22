print('Criação de Conjuntos\n')

conj_A = {1, 2, 3, 4}
print(conj_A)
print(type(conj_A))
print()

conjunto = set({1, 5, 6})
print(conjunto, type(conjunto))

# Não aceita objetos repetidos, imprime elementos únicos
conj_B = {1, 2, 1, 3, 4}
print(conj_B)
print()

print('MÉTODOS DE CONJUNTOS\n')

conj_A.add(8)
print(conj_A)
intersecao = conj_A.intersection(conj_B)
print(intersecao)

print(conj_A - conj_B)

print(conj_B.issubset(conj_A))
print()
# Conjuntos não suportam indexação e nem fatiamento!!!

# União de conjuntos
print(f'A: {conj_A} B: {conj_B} ')
print(conj_A.union(conj_B))

