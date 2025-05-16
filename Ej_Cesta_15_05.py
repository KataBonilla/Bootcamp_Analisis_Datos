cesta={}
continuar=True
while continuar:
    item=input('Introduce un artículo: ')
    precio=float(input('Introduce el precio de '+ item + ': '))
    cesta[item]=precio
    continuar=input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
    