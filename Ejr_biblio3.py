import numpy as np
import matplotlib as plt
from scipy.stats import pearsonr, linregress

#Generar datos para correlación y regresión 
x = np.randow.rand(100)
y = 2 * x + 1 + np.random.randn(100)   #Y = 2x + 1+ ruido
#Calcular correlación
correlation_coefficient, _ = pearsonr(x,y)
#Calcular regresión lineal
slope, intercept, _, _, _ = linregress(x,y)
#Visualización
plot.scatter(x,y, label='DAtos')
plt.plot(x, slope * x + intercept, color='red', label='REgresión Lineal')
plt.title('Corelación y regresión lineal')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

print(f"Coeficiente de Correlación : {correlation_coefficient}")

