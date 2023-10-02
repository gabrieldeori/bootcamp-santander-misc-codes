print("Digite o saldo inicial da conta:")
saldo_atual = float(input())
print("Digite o valor do depósito:")
valor_deposito = float(input())
print("Digite o valor do saque:")
valor_retirada = float(input())


def calc_new_balance(balance, deposit, withdraw):
    new_balance = balance + deposit - withdraw
    print(f"Saldo atualizado na conta: {new_balance:.1f}")
    return new_balance


def main():
    calc_new_balance(saldo_atual, valor_deposito, valor_retirada)


main()
