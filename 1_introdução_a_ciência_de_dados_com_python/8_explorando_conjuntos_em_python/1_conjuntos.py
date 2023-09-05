# criando sets
s1 = set([1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 8, 9])
s2 = set([1, 3, 5, 7, 9])

# união
s3 = s1.union(s2)
print(s3)

# intersecção
s4 = s1.intersection(s2)
print(s4)

# diferença
s5 = s1.difference(s2)
print(s5)

# diferença simétrica
s6 = s1.symmetric_difference(s2)
print(s6)

# subset
s7 = s2.issubset(s1)
print(s7)

# superset
s8 = s1.issuperset(s2)
print(s8)

# disjoint
s9 = s1.isdisjoint(s2)
print(s9)

# acessando dados
s16 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
for valor in s16:
    print(valor)

# É possível acessar convertendo sets em listas
# convertendo sets em listas
sx = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
l2 = list(sx)
print(l2)

# Acessando da lista
print(l2[1])

# convertendo listas em sets
l1 = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8]
s9 = set(l1)
print(s9)

# convertendo tuplas em sets
t1 = (1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8)
s10 = set(t1)
print(s10)

# convertendo sets em tuplas
t2 = tuple(s10)
print(t2)

# convertendo strings em sets
s11 = set('Python')
print(s11)

# convertendo sets em strings
s12 = ''.join(s11)
print(s12)

# convertendo dicionários em sets
d1 = {'chave1': 1, 'chave2': 2, 'chave3': 3}
s13 = set(d1)
print(s13)

# convertendo sets em dicionários
d2 = dict.fromkeys(s13, None)
print(d2)

# convertendo sets em frozensets
s14 = frozenset(s13)
print(s14)

# convertendo frozensets em sets
s15 = set(s14)
print(s15)

# enumerate
s16 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
for indice, valor in enumerate(s16):
    print(indice, valor)

# len
sa = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(len(sa))

# in
sb = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(1 in sb)

# adicionando dados
s17 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s17.add(10)

# removendo dados (Dá erro se o elemento não existe)
s18 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s18.remove(9)
print(s18)

# removendo dados com discard (Não dá erro se o elemento existe)
s19 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s19.discard(9)
print(s19)

# removendo dados com pop
s20 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s20.pop()
print(s20)

# removendo dados com clear
s21 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s21.clear()
print(s21)

# copiando sets com copy
s24 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s25 = s24.copy()
print(s25)

# copiando sets com set
s26 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s27 = set(s26)
print(s27)

# copiando sets com set
s28 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s29 = set(s28)
print(s29)

# atualizando sets com update
s32 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s33 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s32.update(s33)
print(s32)

# atualizando sets com |=
s34 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s35 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s34 |= s35

# atualizando sets com intersection_update
s36 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s37 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s36.intersection_update(s37)

# atualizando sets com &=
s38 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s39 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s38 &= s39

# atualizando sets com difference_update
s40 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s41 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s40.difference_update(s41)

# atualizando sets com -=
s42 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s43 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s42 -= s43

# atualizando sets com symmetric_difference_update
s44 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s45 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s44.symmetric_difference_update(s45)

# atualizando sets com ^=
s46 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s47 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s46 ^= s47
