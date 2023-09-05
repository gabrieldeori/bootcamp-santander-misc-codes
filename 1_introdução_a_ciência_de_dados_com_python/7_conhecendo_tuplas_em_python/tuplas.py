frutas = ("laranja", "banana", "abacate")

letras = tuple("Python")

numeros = tuple([1, 2, 3, 4, 5])

pais = ("Brasil",) # Diferenciar da precedência de operadores em tuplas de um elemento

print(frutas[0])

matriz = ((1, 2), (3, 4), (5, 6))
print(matriz[1][1])

# Fatiamento
print(frutas[1:])
print(frutas[1:2])

# iteração
for fruta in frutas:
    print(fruta)

# Desempacotamento de tuplas
nome, sobrenome, idade = ("João", "Silva", 34)
print(nome)
print(sobrenome)
print(idade)


# Desempacotamento de tuplas com *
nome, sobrenome, *outra_lista = ("João", "Silva", 34, 1.75, 80)
print(nome)
print(sobrenome)
print(outra_lista)

# Métodos tupla
print(frutas.index("banana"))
print(frutas.count("banana"))
print(len(frutas))

carros = ("gol")
print(isinstance(carros, tuple))