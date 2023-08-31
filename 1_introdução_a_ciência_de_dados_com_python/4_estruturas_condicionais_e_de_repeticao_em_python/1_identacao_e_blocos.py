is_true = True
is_false = False

if is_true: # Com o : ele espera a identação. Caso contrário ocorre um erro de sintaxe
    print("is_true é verdadeiro")
    if is_false:
        print("is_false é verdadeiro")
    else:
        print("is_false é falso")
else:
    print("is_true é falso")
    if is_false:
        print("is_false é verdadeiro")
    else:
        print("is_false é falso")

# >>> is_true é verdadeiro
# >>> is_false é falso
 