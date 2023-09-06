# funções
def exibir_mensagem(mensagem='Hello World!'):  # Parâmetro Default
    print(mensagem)


exibir_mensagem()  # Usa parâmetro default
exibir_mensagem('Hello, World!')  # Obrigatoriamente Ordenado
exibir_mensagem(mensagem='Olá, Mundo!')  # Nomeado e Não ordenado

messageDict = {'mensagem': 'Olá, Mundo!'}

exibir_mensagem(**messageDict)  # Desempacotamento de dicionário


# retorno

print(exibir_mensagem())  # None


def somaLista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma


print(somaLista([1, 2, 3, 4, 5]))


# retorno múltiplo
def somaSubtracao(a, b):
    return a + b, a - b


print(somaSubtracao(10, 5))

# retorno múltiplo com desempacotamento
soma, subtracao = somaSubtracao(10, 5)
print(soma, subtracao)


# args e kwargs
def soma(*args):
    soma = 0
    for i in args:
        soma += i
    return soma


print(soma(1, 2, 3, 4, 5))


def soma(**kwargs):
    soma = 0
    for i in kwargs.values():
        soma += i
    return soma


print(soma(a=1, b=2, c=3, d=4, e=5))


# args e kwargs com desempacotamento
def soma(*args, **kwargs):
    soma = 0
    for i in args:
        soma += i
    for i in kwargs.values():
        soma += i
    return soma


print(soma(1, 2, 3, 4, 5, a=1, b=2, c=3, d=4, e=5)) # Observe como foi passado e ele entende que args é uma tupla e kwargs é um dicionário
