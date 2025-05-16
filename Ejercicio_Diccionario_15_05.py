#Programa para el manejo de diccionarios
#Entradas, diccionarios
articulo={1:"Lapiz",2:"Cuadernos",3:"Borrador",4:"Calculadora",5:"Escuadra"}
valores={1:2500,2:3800,3:1200,4:35000,5:3700}

N=int(input("cantidad de articulos comprados: "))
total_compra=0
for i in range(N):
    codigo=int(input("código artículo: "))
    cantidad=int(input("cantidad comprada: "))
    valor_articulo=cantidad*valores.get(codigo)
    total_compra+=valor_articulo
    print("Artículo: ",articulo.get(codigo))
    print("Cantidad comprada: ",cantidad)
    print("Valor unitario: ","{:,.2f}".format(valores.get(codigo)))
    print("Valor total compra: ","{:,.2f}".format(valor_articulo))
print("Valor total compra: ","{:,.2f}".format(total_compra))
