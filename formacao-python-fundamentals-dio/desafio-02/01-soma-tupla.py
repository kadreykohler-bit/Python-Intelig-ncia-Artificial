def soma_tupla(tupla):
    return sum(tupla)  # Aqui está correto!


if __name__ == "__main__":
    entrada = input()  # Recue esta linha!
    # Recue esta também:
    elementos = tuple(map(int, entrada.split()))
    # E estas últimas também:
    resultado = soma_tupla(elementos)
    print(f"A soma dos elementos da tupla é: {resultado}")
