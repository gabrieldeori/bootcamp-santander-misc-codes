# append()
print("append")

lista = []
print(lista)
lista.append(1)
print(lista)
lista.append("Python")
print(lista)
lista.append(True)
print(lista)
lista.append(1.3)
print(lista)
lista.append([1,2,3])
print(lista)

helper = ["hello", "world"]
lista.append(helper)
print(lista)

print("Atenção ao erro abaixo: ")
lista.append(lista) # cuidado com o erro de recursão infinita
print(lista)

# clear
print("clear")
lista.clear()
print(lista)

# copy
print("copy")
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

lista2 = lista
lista2.append(11)
print(lista)
print(lista2)

listaCopy = lista.copy()
lista2.append(1000)
listaCopy.append(12)

print(lista)
print(lista2)
print(listaCopy)

print(id(lista), id(lista2), id(listaCopy))

# count
print("count")
lista = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
print(lista.count(5))
print(lista.count(10))
print(lista.count(100))

# extend
print("extend")
linguagens = ["Python", "Javascript", "C++"]
print(linguagens)
linguagens.extend(["Java", "C", "C#"])
print(linguagens)

linguagens.extend(["C", "PHP"])
print(linguagens) # C aparecerá 2 vezes

# index
print("index")
print(linguagens.index("C++"))
print(linguagens.index("C"))

# insert
print("insert")
linguagens.insert(0, "Assembly")
print(linguagens)

# pop
print("pop")
linguagens.pop()
print(linguagens)

print("pop(0)")
linguagens.pop(0)
print(linguagens)

# remove
print("remove")
linguagens.remove("C") # remove o C de menor índice
print(linguagens)

# reverse

linguagens = ["Python", "Javascript", "C++", "Java", "C", "C#", "C", "PHP", "Assembly"]

print("reverse")
linguagens.reverse()
print(linguagens)

# sort
print("sort")
linguagens.sort()
print(linguagens)

# sort com função
print("sort reverse")
linguagens.sort(reverse=True)
print(linguagens)

# sort pelo tamanho
print("sort tamanho")
linguagens.sort(key=lambda x: len(x))
print(linguagens)

# sort pelo tamanho reverse
print("sort tamanho reverse")
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

# sorted
print("sorted")
print(linguagens)
print(sorted(linguagens))

# len
print("len")
print(len(linguagens))

# lista aleatória 0 a 1000
print("lista aleatória 0 a 1000")
import random
numbers = [random.randint(0, 1000) for x in range(1000)]
print(numbers)

# min

print("min")
print(min(numbers))

# max
print("max")
print(max(numbers))

# sum
print("sum")
print(sum(numbers))

# all
print("all")
print(all([True, True, True, True]))
print(all([True, True, True, False]))

# any
print("any")
print(any([True, True, True, True]))
print(any([True, True, True, False]))


# enumerate
print("enumerate")
for i, x in enumerate(linguagens):
    print(i, x)

# filter
print("filter")
def maiorQueCinco(x):
    return x > 5

print(list(filter(maiorQueCinco, numbers)))

# map
print("map")
def dobro(x):
    return x * 2

print(list(map(dobro, numbers)))

# reduce
print("reduce")
from functools import reduce
def soma(x, y):
    return x + y

print(reduce(soma, numbers))

# zip
print("zip")
lista1 = [1,2,3,4,5]
lista2 = ["a", "b", "c", "d", "e"]
lista3 = ["A", "B", "C", "D", "E"]

print(list(zip(lista1, lista2, lista3)))

# list comprehension
print("list comprehension")
print([x for x in range(10)])
print([x for x in range(10) if x % 2 == 0])
print([x for x in range(10) if x % 2 != 0])

# list comprehension 2
print("list comprehension 2")
print([x for x in range(10) if x % 2 == 0 if x % 3 == 0])
print([x for x in range(10) if x % 2 == 0 if x % 3 == 0 if x % 5 == 0])

# list comprehension 3
print("list comprehension 3")
print([x if x % 2 == 0 else "ímpar" for x in range(10)])
