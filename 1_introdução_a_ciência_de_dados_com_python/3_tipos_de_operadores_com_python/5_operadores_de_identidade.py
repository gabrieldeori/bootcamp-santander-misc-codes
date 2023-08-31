curso = "Curso de Python"
nome_curso = curso
outro_curso = "Curso de Python"
test_a, test_b = 200, 200

print(curso is nome_curso)
# >>> True

print(curso is not nome_curso)
# >>> False

print(outro_curso is curso)
# >>> True

print(test_a is test_b)
# >>> true

outro_curso = "Curso de Python 3"

print("curso:", curso)
print("outro_curso", outro_curso)
# >>> curso: Curso de Python
# >>> outro_curso Curso de Python 3

print(outro_curso is curso)
# >>> False