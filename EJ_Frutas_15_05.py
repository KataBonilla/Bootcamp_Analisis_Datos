Frutas = {'Platano':1.35,'Manzana':0.8,'Pera':0.85,'Naranja':0.7}
fruta = input('¿Qué fruta quieres? ').title()
kg=float(input('¿Cuántos kilos? '))
if fruta in Frutas:
    print(kg, 'kilos de', fruta, 'valen', Frutas[fruta]*kg, '€')
else:
    print("Lo siento, la fruta", fruta, "no esta disponible.")
