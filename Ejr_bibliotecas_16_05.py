import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
#Genera datos aleatorios
data = np.array([10, 15, 12, 8, 17, 14, 15, 10, 12, 16])


#Calcular medidas descriptivas
mean_value = np.mean(data)
median_value = np.median(data)
mode_value = stats.mode(data).mode
std_dev = np.std(data)
variance = np.var(data)
#Imprimir resultados
print(f"media: {mean_value}")
print(f"Media: {median_value}")
print(f"Moda: {mode_value}")
print(f"Desviación estándar: {std_dev}")
print(f"Varianza: {variance}")

plt.hist(data,bins=10)
plt.show()
