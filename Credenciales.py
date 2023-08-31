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