import numpy as np
import matplotlib.pyplot as plt

# Gerar uma sequência de valores de x de -1 a 1
x = np.arange(-1, 1, 0.0001)

# Implementação da fórmula
y1 = np.sqrt(1 - x**2)  # Parte superior do círculo
y2 = -np.sqrt(1 - x**2)  # Parte inferior do círculo

# Plotar o gráfico com as duas partes do círculo
plt.plot(x, y1, 'r')  # Parte superior em vermelho
plt.plot(x, y2, 'r')  # Parte inferior em vermelho

# Adicionar o título do gráfico e os rótulos dos eixos x e y
plt.title("Círculo")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

# Ajustar a escala para que o gráfico tenha proporções corretas
plt.axis('equal')

# Exibir o gráfico
plt.show()

