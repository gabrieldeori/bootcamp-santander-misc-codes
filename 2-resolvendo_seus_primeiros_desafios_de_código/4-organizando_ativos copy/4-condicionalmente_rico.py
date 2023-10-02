DEPLOY_ENVIRONMENT = True


def get_new_balance(balance, withdraw):
    new_balance = balance - withdraw

    return new_balance


def simulateGetBalanceFromDB():
    balance = int(input())

    return balance


def simulateGetWithdrawFromUser():
    if DEPLOY_ENVIRONMENT:
        print("Digite o valor do saque:")

    withdraw = int(input())

    return withdraw


def simulateWithDraw(balance, withdraw):
    success = False

    if (balance >= withdraw):
        new_balance = balance - withdraw
        print(f"Saque realizado com sucesso. Novo saldo: {new_balance}")
        success = True
    else:
        print("Saldo insuficiente. Saque nao realizado!")

    return success


def main():
    saldo_total = simulateGetBalanceFromDB()
    valor_saque = simulateGetWithdrawFromUser()
    simulateWithDraw(saldo_total, valor_saque)


main()
