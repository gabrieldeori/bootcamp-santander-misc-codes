# if elif else - simples
idade = input("Digite sua idade: ")
CRIANCA_IDADE = 12
MAIOR_IDADE = 18
IDOSO_IDADE = 60

if int(idade) >= MAIOR_IDADE:
    print("Você pode tirar carteira de motorista")
else:
    print("Você não pode tirar carteira de motorista")

if int(idade) < CRIANCA_IDADE:
    print("Você é uma criança")
elif int(idade) < MAIOR_IDADE:
    print("Você é um jovem")
elif int(idade) < IDOSO_IDADE:
    print("Você é um adulto")
else:
    print("Você é um idoso")

# if - aninhado
conta_normal = True
conta_universitaria = False
saldo = 1000
cheque_especial = 500
saque = 1499
deve_cheque_especial = 0

if conta_normal:
    if saldo >= saque:
        saldo -= saque
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        calc_saldo = saque - saldo
        cheque_especial = cheque_especial - calc_saldo
        deve_cheque_especial = calc_saldo
        saldo = 0
        print("Saque no cheque especial realizado com sucesso")
    else:
        print("Saldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        saldo -= saque
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")
else:
    print("Conta não encontrada")

print("conta_normal", conta_normal)
print("conta_universitaria", conta_universitaria)
print("Saldo:", saldo)
print("Cheque especial:", cheque_especial)
print("Deve cheque especial:", deve_cheque_especial)

# if - ternário

saldo = 500
saque = 250

print("Saldo:", saldo)
print("Saque:", saque)

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque:", saldo, saque)
