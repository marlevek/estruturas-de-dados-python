# Criação de dicionários
dic1 = {}
dic2 = dict({'a': 12})
dic3 = {'nome': 'Marcelo', 'idade': 51}
print(type(dic1), type(dic2), type(dic3))

pessoa = {
    'nome': 'Marcelo',
    'idade': 51,
}
print(pessoa)

# adicionando valores 
pessoa['profissão'] = 'Cientista de Dados'
print(pessoa)

# buscando chaves
print(pessoa.keys())

# imprimindo os valores
print(pessoa.values())

# imprimindo chaves e valores
print(pessoa.items())

# iterando
for i, c in pessoa.items():
    print(i, c, sep=': ')
print()

contatos = {
    'marcelo_levek@gmailcom': {'nome': 'Marcelo', 'telefone': '41 99417-7854'},
    'carolina@gmailcom': {'nome': 'Carolina', 'telefone': '41 99413-7954'},
    'andrea_levek@gmailcom': {'nome': 'Andrea', 'telefone': '41 99641-7464'},
}
print(contatos['andrea_levek@gmailcom']['telefone'])
print()


