import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt 

#generar datos aleatorios
data = np.array([10, 15, 12, 8, 17, 14, 15, 10, 12, 16])

#Calcular medidas descriptivas
mean_value = np.mean(data)
median_value = np.median(data)

#mode[0]
mode_value = stats.mode(data).mode
std_dev = np.std(data)
variance = np.var(data)

#imprimir resultados
print(f"Media: {mean_value}")
print(f"Medinana:{median_value}")
print(f"Moda: {mode_value}")
print(f"Desviacion estandar: {std_dev}")
print(f"Varianza: {variance}")
plt.hist(data, bins=10)
plt.show()

pr