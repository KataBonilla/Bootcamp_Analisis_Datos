#Conexion.py
import pymysql # libreria que utiliza python para trabajar con la base de datos que tengo en mysql
from pymysql import Error

def obtener_conexion():
    try:
        conexion = pymysql.connect(
            host ='127.0.0.1',
            user = 'root',
            password = 'Colombia2025*',
            database = 'bdg49',
            port = 3306
        )
        print("😋¡Conexión exitosa a MySQL")
        return conexion
    except Error as e:
        print(f'😒Error al conectar a MySQL')
        raise #Re-lanzamos la excepción para manejarla en el llamador

#Código de prueba para verificar la conexión
if __name__ == "__main__":
    conexion = None
    try:
        conexion = obtener_conexion()
        #Ejemplo : crear un cursor y ejecutar una consulta
        with conexion.cursor() as cursor:
            cursor.execute("SELECT VERSION()") #Consulta de prueba
            version = cursor.fetchone()
            print(f"👻 Versión de MySQL: {version[0]}")
    except Error as e:
        print(f"Error durante la  operación: {e}")
    finally:
        #Cerrar la conexión si existe
        if conexion and conexion.open:
            conexion.close()
            print("👌 Conexión cerraada.")

