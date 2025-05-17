#Ley de OHM
# V=I*R
# R=V/I
# I=V/r

'''opcion = input("Escribe 1, 2, o 3: ")
# Voltaje
if opcion == "1":
    I = float(input ("Ingresa la corriente: "))
    R = float(input("Ingresa la resistencia: "))
    V = I * R
    print("El voltaje es: ", V,) 

#Resistencia
elif opcion == "2":
    V = float(input ("Ingresa el voltaje: "))
    I = float(input("Ingresa la Intensidad: "))
    R = V / I
    print("La resistencia es: ", R)

#Intensidad
elif opcion == "3":
    V = float(input("Ingresa el voltaje "))
    R = float(input("Ingresa la resistencia "))
    I = V / R
    print("La intensidad es ", I)

else:
    print ("opcion invalida ")'''   

#Ejercicio profesor
def calcular_voltaje(corriente, resistencia):
    return corriente * resistencia

def calcular_corriente(voltaje, resistencia):
    return voltaje / resistencia

def calcular_resistencia(voltaje, corriente):
    return voltaje / corriente
def main():
    print("Calculadora de la ley de ohm (V = I x R)")
    opcion = input("Que desea calcular? (v=votaje, i=corriente, r=resistencia): ").lower()

    if opcion == 'v':
        i = float(input("ingrese la corriente (I) en amperios: "))
        r = float(input("Ingrese la resistencia (R) en ohmios: "))
        print(f"el voltaje (V) es: {calcular_voltaje(i, r)} voltios")
    elif opcion == 'i':
        v = float(input("ingrese el voltaje (V) en voltios: "))
        r = float(input("ingrese la resistencia(R) en ohmios: "))
        print(f"La corriente (I) es: {calcular_corriente(v, r)} amperios")
    elif opcion == 'r':
        v = float(input("Ingrese el valor de voltaje (V) en voltios"))
        i = float(input("Ingrese la corriente (I) en Amperios: "))
        print(f"La reistencia (R) es: {calcular_resistencia(v, i)} ohmios")
    else:
        print("Error: Opcion no valida. Use 'v', 'i', o 'r'.")

if __name__ == "__main__":
    main()


