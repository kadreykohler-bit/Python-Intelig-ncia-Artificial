# Recebe a entrada e armazena na variável "entrada"
entrada = input()


# Função responsável por filtrar produtos em estoque
def filtrar_produtos_em_estoque(entrada):
    if not entrada:
        return []
    produtos = entrada.split(';')
    produtos_disponiveis = []
    for produto_str in produtos:
        # TODO: Divida a substring do produto em nome, preço e quantidade
        # usando ':' e converta a quantidade para inteiro
        nome, preco, quantidade = produto_str.split(':')
        quantidade = int(quantidade)
        if quantidade > 0:
            produtos_disponiveis.append(produto_str)
        # TODO: Verifique se a quantidade é maior que zero, caso seja adicione
        # o produto à lista de produtos disponíveis

    return produtos_disponiveis

# Imprime a lista de produtos em estoque
    print(filtrar_produtos_em_estoque(entrada))
