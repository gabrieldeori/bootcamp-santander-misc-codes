# Unidimensional

frutas = ["laranja", "maçã", "banana", "melancia"]

frutas = [] # reatribuível

letrasDePython = list("Python") # ['P', 'y', 't', 'h', 'o', 'n']

palavrasPython = list(["Python", "é", "uma", "linguagem", "excelente"])

numerosZeroNove = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

carro = ["Fusca", 1976, "Volkswagen", 1.3, True]

print(frutas)
print(letrasDePython)
print(palavrasPython)
print(numerosZeroNove)
print(carro)

print(numerosZeroNove[0])
print(palavrasPython[1:3])
print(carro[-1])

# Matrizes

matriz = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]

print(matriz)
print(matriz[0])
print(matriz[1][1])

matriz3d = [
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ],
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ],
]

print(matriz3d)
print(matriz3d[0])
print(matriz3d[1][1])
print(matriz3d[1][1][1])

# Fatiamento 3D
print(matriz3d[0][0:2:2][-1])
print(matriz3d[0][0:2:2][-1][1])

# Iterações

print("\n\n Iterações:")
for x in matriz3d:
    print("\n\n")
    print("x")
    print(x)
    for y in x:
        print("y: ", y)
        for z in y:
            print("z: ", z)

pares = [numero for numero in range(10) if numero % 2 == 0]
print(pares)
