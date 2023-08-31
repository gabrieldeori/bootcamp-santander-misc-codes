curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso
# >>> True

"python" in curso
# >>> False

"Maçã" in frutas
# >>> False

"laranja" in frutas
# >>> True

"Laranja" in frutas
# >>> False

200 in saques
# >>> False

"Python" not in curso
# >>> False

"Maçã" not in frutas
# >>> True

200 not in saques
# >>> True
