# Copy
contatos = {
   ' marcelo_levek@gmail.com': {
       'nome': 'Marcelo', 
       'cel': '41 99674-8547',
   }
}
copia = contatos.copy()
print(copia)
copia['marcelo_levek@gmail.com'] = {'nome': 'Mar'}
print(copia)

dic = dict.fromkeys(['nome', 'idade'])
print(dic)
dic1 = dict.fromkeys(['nome', 'idade'], 'vazio')
print(dic1)

print(contatos.get('nome'))
resultado = contatos.get('marcelo_levek@gmail.com', {})
print(resultado)

contatos.update({'sexo': 'M'})
print(contatos)

contatos.setdefault('idade', 52)
print(contatos)

