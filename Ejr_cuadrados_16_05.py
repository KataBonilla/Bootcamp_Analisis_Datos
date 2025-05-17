#funcion para calcular los ciadrados de una lista de numeros 
def square(sample):
    list=[]
    for i in sample:
        list.append(i**2)
    return list
print(square([1,2,3,4,5]))
print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

"""Función que calcula la media, varianza y desviación tipica de los numeros en sample
parametros
sample: Es una lista de numeros
Devuelve un diccionario con la media, varianza y desviación tipica de los numeros en sample
"""
def statistics(sample):
    stat={}
    stat['media']=sum(sample)/len(sample)
    stat['varianza']=sum(square(sample))/len(sample)-stat['media']**2
    stat['desviación']=stat['varianza']**0.5
    return stat
print(statistics([1,2,3,4,5]))
print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))