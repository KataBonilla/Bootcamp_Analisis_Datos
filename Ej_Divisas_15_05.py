#Ejercicio para mostrar la divisa de una moneda
monedas={'Euro':'€','Dollar':'$','Yen':'¥'}
moneda=input("Introduce una divisa: ")
print(monedas.get(monedas.title(), "La divisa no esta"))
