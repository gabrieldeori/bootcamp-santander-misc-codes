def compareValueReturnMessage(valor):

    if valor > 0:
        return f"Deposito realizado com sucesso!\n Saldo atual: R$ {valor:.2f}"
    elif valor != 0:
        return "Valor invalido! Digite um valor maior que zero."
    return "Encerrando o programa..."


def main():
    valor = float(input())
    message = compareValueReturnMessage(valor)
    print(message)


main()
