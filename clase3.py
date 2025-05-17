#ejercico3

'''def circle_area(radius):
    """Funcion que calcula el area de un circulo.
    parametros
    radius: es el radio del circulo"""

    pi = 3.1414
    return pi*radius**2

def cilinder_volume(radius, high):
    """Funcion que calcula el volumen de un cilindro.
    parametros
    devuelve el volumen del cilindro de radio radius y altura high""" 

    return circle_area(radius)*high

print(cilinder_volume(3,5))'''

#ejercicio 4

'''def mean(samplee):
    """Funcion que calcula la media de una miestra de numeros.
    parametros
    simple: Es una lista de numeros
    Devielve la media de los numeros en sample"""

    return sum(samplee)/len(samplee)

print(mean ([1, 2, 3, 4, 5]))
print(mean([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))'''

#ejercicio5

'''def square(sample):
    """Funcion que calcula cuadrados de una lista de numeros
    parametros
    sample:Es una lista de numeros
    Devuelve una lista con los cuadrados de los numeros de la lista sample."""

    list =[]
    for i in sample:
        list.append(i**2)
    return list
print(square([1,2,3,4,5]))
print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))'''

#ejercicio6

def square(sample):
    """Funcion que calcula los cuadrados de una lista de numeros.
    parametros
    sample: Es una lista de numeros
    devuelve una lista con los cuadrados de los numeros de la lista sample"""

    list = []
    for i in sample:
        list.append(i**2)
    return list

def statistics(sample):
    """Funcion que calcula la media, varianza y desviacion tipica de una muestra de numeros.
    Parametros
    Sample:Es una lista de numeros
    Devielve un diccionario con la media, varianza y desciacion tipica de los numeros en sample""" 
    
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum (square(sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics([1, 2, 3, 4, 5]))
print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
