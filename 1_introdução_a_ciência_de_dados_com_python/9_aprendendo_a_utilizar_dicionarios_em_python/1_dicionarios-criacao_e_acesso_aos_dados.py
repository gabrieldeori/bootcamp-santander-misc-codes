# dicts
d1 = dict({'chave1': 'valor da chave'})
print(d1)

d2 = {'chave1': 'valor da chave'}
print(d2)

d1['nova_chave'] = 'valor da nova chave'
print(d1)

d1['nova_chave'] = 'valor da nova chave alterado'
print(d1)

outraChave = 'outra_chave'
d1[outraChave] = 'valor da outra chave'
print(d1)

# acesso aos dados
d3 = {'chave1': 'valor da chave', 'chave2': 'valor da chave 2'}
print(d3['chave1'])

# acessando chaves
print(d3.keys())

# acessando valores
print(d3.values())

# acessando itens
print(d3.items())

# Aninhamento
d4 = {'chave1': {'chave2': 'valor da chave 2'}}
print(d4['chave1']['chave2'])

# iterando sobre dicionários
for k in d3:
    print(k)

for k in d3:
    print(d3[k])

for i in d3.items():
    print(i) # lista de tuplas

for k, v in d3.items():
    print(k, v)

for k in d3.keys():
    print(k)

for v in d3.values():
    print(v)

# verificando se uma chave existe
print('chave1' in d3)
print('chave3' in d3)

