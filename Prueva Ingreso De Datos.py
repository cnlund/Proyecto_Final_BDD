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



# Configura la cadena de conexión a tu base de datos SQL Server
conexion = pyodbc.connect(f"Driver=ODBC Driver 17 for SQL Server; \nServer={usuario}; \nDatabase=Biblioteca; \nTrusted_Connection=yes;")

cursor = conexion.cursor()

try:
    # Captura de datos desde el usuario
    libro_id = input("Ingrese el valor para Libro_id: ")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    fecha_publicacion = input("Ingrese la fecha de publicación del libro (DD/MM/AAAA): ")
    estado = input("Ingrese el estado del libro (1 para disponible, 0 para no disponible): ")

    # Validaciones de tipos de datos
    try:
        libro_id = int(libro_id)
        estado = int(estado)
    except ValueError:
        print("Error: Libro_id y estado deben ser números enteros (1 para disponible, cualquier otro numero para no disponible)")
        exit(1)

    # Inserta los datos en la tabla "Libro"
    cursor.execute("INSERT INTO Libro (Libro_id, Libro_titulo, Libro_autor, Libro_fecha_publicacion, Libro_estado) VALUES (?, ?, ?, ?, ?)",
                   (libro_id, titulo, autor, fecha_publicacion, estado))

    # Confirma los cambios en la base de datos
    conexion.commit()
    print("Registro insertado exitosamente en la tabla 'Libro'.")

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Cierra el cursor y la conexión a la base de datos
    cursor.close()
    conexion.close()