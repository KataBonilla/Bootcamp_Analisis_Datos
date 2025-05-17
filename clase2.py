#programa para calcular la cantidad de palabras de una frase

'''frase=input("Fease: ")
can_palabras=len(frase.split() )
print("cantidad de palabras: ", can_palabras)'''

#PROGRAMA PARA CONTAR PALABRAS DE CADA ELEMENTO DE UNA LISTA DE NOMBRES

"""lista_nombres=[]
lista_cantidad=[]
nombre=input("Nombre completo de la persona: ")
while nombre!="fin":
    lista_nombres.append(nombre)
    nombre=input("Nombre completo de la persona: ")
for i in lista_nombres:
    cantidad_palabras=len(nombre.split())
    lista_cantidad.append(cantidad_palabras)
print("Lista nombres: ", lista_nombres)
print("Lista cantidad de palabras: ", lista_cantidad)"""

"""subjects = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
for subject in subjects:
    print("Yo estudio " + subject)"""

'''subjects = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("Que nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])'''

#programa de listas dentro de listas

#llenar la lista dentro de lista (matriz)

'''numeros=[]
for i in range(2) :
    numeros.append([])
    for j in range(2) :
        numeros[i] .append(int(input("Numero:" )))
#imprimir lista dentro de lista (matriz)
print(numeros)
#procesar lista dentro de lista
cpares=0
cimpares=0
for i in range(2):
    for j in range(2):
        if numeros[i] [j]%2==0 :
            cpares+=1
        else:
            cimpares+=1
print("Cantidad de pares: ",cpares)
print("Cantidad de impares: ", cimpares)'''

#PROGRAMA PARA MANEJO DE DICCIONARIOS
#DICCIONARIOS
"""articulos={1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
valores={1:2500,2:3800,3:1200,4:35000,5:3700}

N=int(input("cantidad de articulos comprados: "))
total_compra=0
for i in range(N) :
    codigo=int(input("Codigo articulo: "))
    cantidad=int(input("Cantidad comprada: "))
    valor_articulo=cantidad*valores.get(codigo)
    total_compra+=valor_articulo
    print("Articulo: ",articulos.get(codigo))
    print("Cantidad comprada: ",cantidad)
    print("valor unitario: ","{:,.2f}".format(valores.get(codigo)))
    print("Valor articulo: ","{:,.2f}".format(valor_articulo))
print("Valor total compra: ","{:,.2f}".format(total_compra))"""

#Ejercicio1

'''monedas = {'Euro':'€', 'Dollar':'$', 'yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no esta."))'''

#Ejercicio2

'''nombre = input('Como te llamas? ')
edad = input('Cuantos annos tienes? ')
direccion = input('Cual es tu doreccion? ')
telefono = input('Cual es tu numero de telefono ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'annos, vive en', persona['direccion'], 'y su numero de telefono es', persona['telefono'])'''

#Ejercicio3

"""frutas = {'Platano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('Que fruta quieres? ').title()
kg = float(input('Cuantos kilos? '))
if fruta in frutas:
    print(kg, 'Kilos de', fruta, 'Valen', frutas[fruta]*kg,'$')"""

#Ejercicio4

'''meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 10:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])'''
