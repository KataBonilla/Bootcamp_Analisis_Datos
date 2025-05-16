#Programa para solicitarle al uu¿suario sus datos personales
nombre=input("¿Cuál es tu nombre? ")
edad=input("¿Cuántos años tienes? ")
direccion=input("¿E dónde vives? ")
telefono=input("¿Cuál es tu número de telefono? ")
persona={'nombre':nombre,'edad':edad,'dirección':direccion,'telefono':telefono}
print(persona['nombre'],'tiene',persona['edad'],'años, vive en',persona['direccion'],'y su numero de celular es',persona[telefono])
