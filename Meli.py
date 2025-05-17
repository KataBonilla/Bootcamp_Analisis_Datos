print("Hola campistas")
#lenguaje de programacion python
#dado la base y la altura de un triangulo, calcular y mostrat su area, a traves de la formula area = (base*altura)
# el imput se usa para la entrada de un valor
# el print es la salida, lo que se visualiza

#Programa para calcular el area de un triangulo
#Autor: Melissa F
#Fecha: 13/05/2025

"""Base=float(input("ingrese Base: ")) 
altura=float (input("Ingrese altura: "))

# proceso
area=(Base*altura)/2

#salida
print("El area es: ", area)"""

# Programa para calcular nota definitiva de un tripulante 
# Autor: Melissa F
# Fecha

"""n1=float(input("Nota reto 1: "))
n2=float(input("Nota reto 2: "))
n3=float(input("Nota reto 3: "))
n4=float(input("Nota reto 4: "))
n5=float(input("Nota reto 5: "))
ni=float(input("Nota Ingles: "))
nd=n1*0.1+n2*0.1+n3*0.2+n4*0.2+n5*0.2+ni*0.2
print("Nota definitiva: ",'{:,.2f}'.format(nd))"""

#Programa para calcular subsidio de transporte

"""nombre= input("Nombre empleado: ")
salario=float(input("Salario "))

if salario<=1000000:
    subsidio=120000
else:
    subsidio=0

print("Nombre empleado: ", nombre)
print("Salario: ", '{:,.2f}' .format(salario))
print("Subsidio de transporte: ", '{:,.2f}'.format(subsidio))"""

#PROGRAMA PARA CALCULAR EVALUACION CUALITATIVA

"""nombre=input("Nombre del estudiante: ")
eva_cuantitativa=int(input("Evaluacion cuantitativa: "))

if eva_cuantitativa<=59:
    eva_cualitativa="D"
elif eva_cuantitativa<=79:
    eva_cualitativa="C"
elif eva_cuantitativa<=89:
    eva_cualitativa="B"
else:
    eva_cualitativa="A"

print("Nombre estudiante: ", nombre)
print("Evaluacion cuantitativa: ", eva_cuantitativa)
print("Evaluacion cualitativa: ", eva_cualitativa)"""

#PROGRAMA PARA CALCULAR EL VALOR DE SERVICIO DE AGUA

"""N=int (input("Cantidad de usuarios: "))
for i in range(N) :
    codigo=int(input("codigo usuario: "))
    nombre=input("nombre: ")
    estado=input("Estado (V=Vigente, S+Suspendido) : ")
    estrato=int(input("Estrato (1,2,3,4,5,6) : "))
    consumo=float(input("consumo del mes: "))
    if estado=="V":
        if estrato==1:
            tarifa_basica=10000
        elif estrato==2:
            tarifa_basica=20000
        elif estrato==3:
            tarifa_basica=30000
        elif estrato==4:
            tarifa_basica=45000
        elif estrato==5:
            tarifa_basica=60000
        else:
            tarifa_basica=70000
        valor_consumo=consumo*200
        valor_pagar=tarifa_basica+valor_consumo
        print("Nombre usuario: ", nombre)
        print("Tarifa basica: ", '{:,.2f}'.format(tarifa_basica))
        print("Valor consumo: ", '{:,.2f}'.format(valor_consumo))
        print("Valor a Pagar: ", '{:,.2f}'.format(valor_pagar))"""

#PROGRAMA PARA HALLAR PARES E IMPARES

"""can_pares=0
can_impares=0
num=int(input("Numero entero: "))
while num!=-1:
    if num%2==0 :
        print(num,"es PAR")
        can_pares+=1
    else:
        print(num," es IMPAR")
        can_impares+=1
    num=int(input("Numero entero: "))
print("Cantidad de pares: ", can_pares)
print("Cantidad de impares: ", can_impares)"""

"""word = input("Introduce una palabra: ")
for i in range(10):
    print(word)"""
    
age = int(input("how old are you?"))
for i in range(age):
    print("you are " + str(i+1) + " years old")

