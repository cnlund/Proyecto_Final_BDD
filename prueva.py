import pyodbc
#Aqui insertamos los datos de la base de datos de la que vamos a extraer la data

while True:
    usuario = input(""" 
¿Quién prueba el código?
1. Jub1101
2. Cnlund       

Ingreso:  """)

    if usuario == "1":
        usuario = "DESKTOP-F5TMUR9"
        break  # Rompe el bucle si el usuario ingresa un valor válido
    elif usuario == "2":
        usuario = "DESKTOP-MR17TOI\MSSQLSERVER01"
        break  # Rompe el bucle si el usuario ingresa un valor válido
    else:
        print("Opción no válida. Debes ingresar '1' o '2'.")

# Después de esta parte, la variable 'usuario' tendrá el valor "DESKTOP-F5TMUR9" si se eligió 1 o 2.


datosbdd = f"Driver=ODBC Driver 17 for SQL Server; \nServer={usuario}; \nDatabase=Biblioteca; \nTrusted_Connection=yes;"
print (datosbdd)



################################################  Me canicas de busqueda de usurios ################################################

#Establecemos la conneccion con la BDD a traves de pyodbc y las credenciales almacenadas en otro archivo
conn = pyodbc.connect(datosbdd)

# Crea un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Solicita al usuario que ingrese el texto a buscar ‼️ OJO AL PIOJO ‼️ no c como ballas ha hacer la funcion de activacion con la libreria
Cliente_email = input("Ingrese el Correo del Cliente: ")

# Consulta SQL para buscar el texto en la columna 'Cliente email' y obtener los resultados
query = f"SELECT * FROM Cliente WHERE [Cliente_email] LIKE '%{Cliente_email}%'"

# Ejecuta la consulta
cursor.execute(query)

# Inicializa un arreglo para almacenar los resultados
Resultados_Cliente_emai = []

# Itera a través de las filas de resultados y agrega cada fila formateada a 'resultados'
for row in cursor:
    resultado_formateado = tuple(map(str, row))  # Convierte todos los elementos a cadenas
    Resultados_Cliente_emai.append(resultado_formateado)

# Cierra el cursor y la conexión
cursor.close()
conn.close()

# Muestra los resultados encontrados
if len(Resultados_Cliente_emai) > 0:
    print("Resultados encontrados:")
    for row in Resultados_Cliente_emai:
        print(row)
else:
    print("No se encontraron resultados para el texto ingresado.")

####################################################################################################################################