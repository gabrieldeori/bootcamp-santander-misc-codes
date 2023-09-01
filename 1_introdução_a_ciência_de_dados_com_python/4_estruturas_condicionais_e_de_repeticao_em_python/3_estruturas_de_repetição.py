# for iterável
texto = "Abacate doce e gostoso de comer com limão, sal e açúcar"
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra.upper(), end="")
else :
    print("Final do for") # Executa no final

numero = 20

print(list(range(numero)))
print(list(range(5, numero)))
print(list(range(0, numero, 2)))
print(list(range(3, numero, 2)))

# for range
for numero in range(numero):
    print(numero, end=" ")
else :
    print("Final do for")

# while
opcao = -1

while opcao != 0:
    opcao = int(input("Digite 0 e aperte enter pra sair: "))
    print(f"Você digitou {opcao}")
else :
    print("Final do while")

# break
while True:
    opcao = int(input("Digite 0 e aperte enter pra sair: "))
    if opcao == 0:
        break

for numero in range(100):
    if numero == 10:
        break
    print(numero, end=" ")
else :
    print("Final do for")

# continue
for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")
else :
    print("Final do for")
