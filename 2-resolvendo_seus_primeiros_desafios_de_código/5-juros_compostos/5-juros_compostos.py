valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())


def me_recuso_a_iterar_em_algo_tao_trivial(initial_value, interest_rate, period):
    final_value = initial_value
    for _ in range(period):
        final_value = final_value + (final_value * interest_rate)
    return final_value

# Programador tem que aprender a se armar com argumentos matemáticos para evitar
# Sobrecarregar os sistemas. O código que foi pedido é uma solução que não é eficiente.


valor_final = valor_inicial * (1 + taxa_juros) ** periodo


print(f"Valor final do investimento: R$ {valor_final:.2f}")
