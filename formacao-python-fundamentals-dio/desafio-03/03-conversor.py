class ConversorTemperatura:
    def celsius_para_fahrenheit(self, celsius):
        # Aqui aplicamos a fórmula: (C * 1.8) + 32
        return (celsius * 1.8) + 32


# Entrada do usuário
celsius = float(input())

# Criando a instância do conversor
conversor = ConversorTemperatura()

# Chamando o método e imprimindo o resultado
fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)
