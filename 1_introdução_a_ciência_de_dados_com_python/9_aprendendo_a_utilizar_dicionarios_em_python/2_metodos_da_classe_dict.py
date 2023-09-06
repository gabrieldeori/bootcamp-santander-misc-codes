# dict methods

d1 = dict({'chave1': 'valor da chave'})
print(d1)

# setdefault
d1.setdefault('chave2', 'valor da chave 2')
print(d1)

# clear
d1.clear()

# copy
d2 = {'chave1': 'valor da chave'}
d3 = d2.copy()
print(d3)

# fromkeys
d4 = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(d4)

# fromkeys sem valor
d4 = {}.fromkeys(['teste', 'teste2'])
print(d4)

# get
d5 = {'nome': 'Gabriel', 'pontos': 100}
print(d5.get('nome'))

# print(d5["chaveInexistente"]) Gera erro

print(d5.get('chaveInexistente')) # Não gera erro, retorna none

print(d5.get('nonExistentKey'), {}) # Não gera erro, retorna {}

# update
d11 = {'nome': 'Gabriel', 'pontos': 100}
d11.update({'nome': 'Gabriel', 'pontos': 100})

# pop
d8 = {'nome': 'Gabriel', 'pontos': 100}
print(d8.pop('nome')) # Se não encontra a chave, gera erro
print(d8.pop('chaveInexistente', 'chave não existe')) # Não gera erro, retorna a mensagem

# popitem
d9 = {'nome': 'Gabriel', 'pontos': 100}
print(d9.popitem(), 'chave não existe')

# del
d5 = {'nome': 'Gabriel', 'pontos': 100}
del d5['nome']
del d5 # apaga o dicionário inteiro

# items
d6 = {'nome': 'Gabriel', 'pontos': 100}
print(d6.items())

# keys
d7 = {'nome': 'Gabriel', 'pontos': 100}
print(d7.keys())

# values
d12 = {'nome': 'Gabriel', 'pontos': 100}
print(d12.values())

# count com keys
d5 = {'nome': 'Gabriel', 'pontos': 100}
lista_chaves = list(d5.keys())
print(lista_chaves.count('nome'))

# in
d5 = {'nome': 'Gabriel', 'pontos': 100}
print('nome' in d5)

d5 = {'nome': { 'first_name': 'Gabriel' }, 'pontos': 100}
print('first_name' in d5['nome'])

# not in
d5 = {'nome': 'Gabriel', 'pontos': 100}
print('nome' not in d5)
