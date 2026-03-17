limite = float(input())
# Recebe a string de transações como entrada do usuário
transacoes = input()


# Define a função para filtrar transações acima do limite especificado
def filtrar_transacoes_acima_do_limite(limite, transacoes):
    if not transacoes:
        return []

    transacoes_filtradas = []
    lista_transacoes = transacoes.split(';')
    # Itera sobre cada transação na lista de transações
    for transacao in lista_transacoes:
        id_transacao, valor_str = transacao.split(':')
        valor = float(valor_str)
        if valor > limite:
            transacoes_filtradas.append(f"{id_transacao}:{valor}")
        # TODO: Compare o valor da transação com o limite e adiciona à lista
        # filtrada se for maior

    return transacoes_filtradas
# Imprime as transações com valores acima do limite
    print(filtrar_transacoes_acima_do_limite(limite, transacoes))
