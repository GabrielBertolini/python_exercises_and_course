# Dados fornecidos
classes = [(15, 25), (25, 35), (35, 45), (45, 55), (55, 65)]
frequencia = [16, 30, 41, 28, 15]

# Cálculo dos pontos médios
pontos_medios = [(limite[0] + limite[1]) / 2 for limite in classes]

# Cálculo da média amostral
n = sum(frequencia)
media = sum(f * x for f, x in zip(frequencia, pontos_medios)) / n

# Cálculo da variância amostral (dividindo por n-1)
variancia_amostral = sum(f * (x - media) ** 2 for f, x in zip(frequencia, pontos_medios)) / (n - 1)

# Cálculo do desvio padrão amostral
desvio_padrao_amostral = variancia_amostral ** 0.5
print(desvio_padrao_amostral)


