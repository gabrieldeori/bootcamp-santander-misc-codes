#  Parâmetros especiais
#  def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):


def criar_carro(modelo, ano, placa, /, marca, motor, *, combustível):
    print(modelo, ano, placa, marca, motor, combustível)


criar_carro(
    'Gol', 2012, 'AAA-1111', marca='Volkswagen',
    motor=1.0, combustível='Flex'
)  # Válido

# criar_carro('Gol', 2012, 'AAA-1111', 'Volkswagen', 1.0, 'Flex') # inválido
# criar_carro(modelo='Gol', ano=2012,
# marca='AAA-1111', 'Volkswagen', 1.0, 'Flex')  # Inválido


def criar_carro_only_keyword(*, modelo, ano, placa, marca, motor, combustível):
    print(modelo, ano, placa, marca, motor, combustível)


criar_carro_only_keyword(
    modelo='Gol',
    ano=2012, placa='AAA-1111',
    marca='Volkswagen',
    motor=1.0,
    combustível='Flex'
)  # Válido

# criar_carro_only_keyword(
#   'Gol', 2012, 'AAA-1111',
#   'Volkswagen', 1.0, 'Flex'
# ) # Inválido
# criar_carro_only_keyword(
#   modelo='Gol', ano=2012, marca='AAA-1111',
#   'Volkswagen', 1.0, 'Flex'
# )  # Inválido
# criar_carro_only_keyword(
#   'Gol', 2012, 'AAA-1111', marca='Volkswagen',
#   motor=1.0, combustível='Flex'
# )  # Inválido


#  Objetos de primeira classe
def onlyInt(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return True
    return False


def onlyFloat(a, b):
    if isinstance(a, float) and isinstance(b, float):
        return True
    return False


def validateAndSum(a, b, validate):
    if validate(a, b):
        return a + b
    return 'Não foi possível somar'


print(validateAndSum(1, 2, onlyInt))
print(validateAndSum(1.0, 2.0, onlyFloat))
print(validateAndSum(1, 2.0, onlyInt))
print(validateAndSum(1.0, 2, onlyFloat))


outrafuncao = validateAndSum  # Posso atribuir uma função a uma variável
print(outrafuncao(1, 2, onlyInt))


# Funções aninhadas
def funcaoExterna():
    print('Executando função externa')

    def funcaoInterna():
        print('Executando função interna')

    funcaoInterna()


funcaoExterna()


# Escopo local e escopo global
salario = 4000
print(salario)


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


print(salario_bonus(1000))
print(salario)


def salario_pay(amount):
    salario = 10000
    salario -= amount
    return salario


print(salario_pay(1000))
print(salario)


# Funções e listas
lista = [1, 2, 3, 4, 5]


# Inicializando lista dentro de função
def funcao():
    lista = [0]  # inicializar lista dentro de função será uma lista local
    lista.append(6)  # Não altera
    return lista


print("Inicializando lista dentro de função")
print(lista)
print(funcao())
print(lista)


# Não inicializando lista dentro de função
def funcao1():
    lista.append(6)  # Altera
    return lista


print("Não inicializando lista dentro de função")
print(lista)
print(funcao1())
print(lista)


# Lista como parâmetro
def funcao2(lista):
    lista.append(7)  # Altera
    return lista


print("Lista como parâmetro")
print(lista)
print(funcao2(lista))
print(lista)


# usando .copy
def funcao3():
    listaAux = lista.copy()
    listaAux.append(8)  # Não altera
    return listaAux


print("Usando .copy")
print(lista)
print(funcao3())
print(lista)


# usando parâmetro e .copy
def funcao4(lista):
    listaAux = lista.copy()
    listaAux.append(9)  # Não altera
    return listaAux


print("Usando parâmetro e .copy")
print(lista)
print(funcao4(lista))
print(lista)
