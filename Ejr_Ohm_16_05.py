#Programa para la ley de Ohm
def voltaje(I,R):
    return I*R
#print(voltaje(2,3))

def corriente(V,R):
    return V/R
#print(corriente(4,2))

def resistencia(V,I):
    return V/I
#print(resistencia(8,4))

def ley_ohm(): #se utiliza para poder llamar esta función en otros archivos
    print("Calculadora de Ley de Ohm (V=R*I)")
    usuario =input("¿Qué deseas calcular? (V=voltaje, I=corriente o R=resistencia)")
    if usuario =='V':
        I=float(input("Ingrese la corriente (I) en amperios: "))
        R=float(input("Ingrese la resistencia (R) en ohms: "))
        print("El voltaje (V) es: ",voltaje(I,R) )

    elif usuario == 'I':
        V=float(input("Ingrese el valor de la tensión (V) en voltios: "))
        R=float(input("Ingrese el valor de la resistencia en ohms: "))
        print("La corriente (I) es: ",corriente(V,R))

    elif usuario == 'R':
        V=float(input("Ingrese el valor del voltaje (V) en voltios: "))
        I=float(input("Ingrese el valor de la corriente (I) en amperios: "))
        print("La resistencia (R) es: ",resistencia(V,I))
    else:
        print("Error, opción no válida. Use V, I o R")


if __name__ == "__ley_ohm__":
    ley_ohm()