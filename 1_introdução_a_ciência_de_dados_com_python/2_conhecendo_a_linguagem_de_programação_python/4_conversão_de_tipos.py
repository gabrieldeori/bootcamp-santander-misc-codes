# int > float
print("int > float")
var_to_convert = 10
var_to_convert = float(var_to_convert) # Usando método
print(var_to_convert)
print(type(var_to_convert))

print("\n")

var_to_convert = 10
var_to_convert = var_to_convert / 1 # Usando divisão
print(var_to_convert)
print(type(var_to_convert))
print("\n\n")

# float > int
print("float > int")
var_to_convert = 10.5
var_to_convert = int(var_to_convert) # Usando método (Perde o float)
print(var_to_convert)
print(type(var_to_convert))
print("\n\n")

# num > string
print("num > string")
var_to_convert = 10.3
var_to_convert = str(var_to_convert)
print(var_to_convert)
print(type(var_to_convert))
var_to_convert = 10.5
converted = f"something {var_to_convert} something"
print("\n\n")

# string > num
print("string > num")

var_to_convert = "10.5"
var_to_convert = float(var_to_convert)
print(var_to_convert)
print(type(var_to_convert))
print()

var_to_convert = "10"
var_to_convert = int(var_to_convert)
print(var_to_convert)
print(type(var_to_convert))
print("\n\n")

# Pra dar certo 10.5 string pra int, primeiro pra float, depois pra int e depois pra string
print("Pra dar certo 10.5 string pra int, primeiro pra float, depois pra int e depois pra string")
var_to_convert = "10.5" # Pra int falha
var_to_convert = float(var_to_convert)
var_to_convert = int(var_to_convert)
print(var_to_convert)
print(type(var_to_convert))
print("\n\n")

print("Casos de falha")
print("\n\n")

# Porém caso a string não seja tipo numérico
# A conversão falha e retorna erro

var_to_convert = "10.5" # Falha pra int
var_to_convert = int(var_to_convert)
print(var_to_convert)
print(type(var_to_convert))

# Falha pra int e float
var_to_convert = "dez"
var_to_convert = int(var_to_convert)
print(var_to_convert)
print(type(var_to_convert))

var_to_convert = "dez"
var_to_convert = float(var_to_convert)
print(var_to_convert)
print(type(var_to_convert))
