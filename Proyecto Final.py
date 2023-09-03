#Aqui importamos todos los archivos o bibliotecas que vamos a necesitar para poder ejecutar el programa
from Credenciales import datosbdd
import pyodbc
import tkinter as tk
from tkinter import PhotoImage
from tkinter import font

#Establecemos la conneccion con la BDD a traves de pyodbc y las credenciales almacenadas en otro archivo
conn = pyodbc.connect(datosbdd)

#Usamos tkinter para crear la ventana en la que se mostrara el programa y le damos el atributo -fullscreen
bdd = tk.Tk()
bdd.title("Proyecto Final BDD")
bdd.attributes("-fullscreen", True)

################################ En esta zona iran los comandos de pyodbc que se necesitan ejecutar ################################

#Creamos una funcion que imprima la lista de libros disponibles
def tabla_libros_disponibles(contenedor):
    crear_titulo(contenedor,"Libros",2,1,18)
    crear_titulo(contenedor,"Disponibles",3,1,18)
    crear_lista(contenedor,"ID",1,2, 5)
    crear_lista(contenedor,"Titulo",2,2,18)
    crear_lista(contenedor,"Autor",3,2,18)
    crear_lista(contenedor,"Fecha de Publicacion",4,2,20)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Libro WHERE Libro.Libro_estado = 1")
    i=3
    for row in cursor:
        crear_lista(contenedor,row.Libro_id,1, i, 5)
        crear_lista(contenedor,row.Libro_titulo,2,i,18)
        crear_lista(contenedor,row.Libro_autor,3,i,18)
        crear_lista(contenedor,row.Libro_fecha_publicacion,4,i,20)
        i=i+1

#Creamos una funcion que imprima la lista de clientes existentes
def tabla_clientes_existentes(contenedor):
    crear_titulo(contenedor,"Lista de",2,1,18)
    crear_titulo(contenedor,"Clientes",3,1,18)
    crear_lista(contenedor,"ID",1,2,5)
    crear_lista(contenedor,"Nombre",2,2,18)
    crear_lista(contenedor,"Correo",3,2,18)
    crear_lista(contenedor,"Telefono",4,2,18)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cliente")
    i=3
    for row in cursor:
        crear_lista(contenedor,row.Cliente_id,1, i, 5)
        crear_lista(contenedor,row.Cliente_nombre,2,i,18)
        crear_lista(contenedor,row.Cliente_email,3,i,18)
        crear_lista(contenedor,row.Cliente_tel,4,i,18)
        i=i+1

#Creamos una funcion que busque un cliente en especifico
def buscar_cliente(correo):
    cursor = conn.cursor()
    query = ("SELECT * FROM Cliente WHERE Cliente_email LIKE (CAST(? AS VARCHAR(50)))")
    cursor.execute(query, f"%{correo}%")
    busqueda = cursor.fetchall()
    if not busqueda:
        crear_lista(Respuesta,"No se ha encontrado un Cliente que coincida",1,1,50)
    else:
        for row in busqueda:
            crear_lista(Respuesta,row.Cliente_id,1, 1, 5)
            crear_lista(Respuesta,row.Cliente_nombre,2,1,18)
            crear_lista(Respuesta,row.Cliente_email,3,1,18)
            crear_lista(Respuesta,row.Cliente_tel,4,1,18)

####################################################################################################################################

############################## En esta zona iran los comandos de los botones que vallamos a utilizar ###############################

#Definimos una funcion que cuando se pulse ese boton destruya la ventana
def cerrar_bdd():
    bdd.destroy()

#Definimos una funcion que desaparezca el menu inicial y llame a la pantalla de inicio
def cambio_ventana1():
    Menu_inicial.place_forget()
    Ventana_1.place(x=0,y=0,relwidth=1,relheight=1)

#Definimos una funcion que cree un label para las tablas
def crear_lista(contenedor,texto, columna, fila, ancho):
    label = tk.Label(contenedor,text=texto,bg="#F5F5F5",pady=5, width=ancho)
    label.grid(row=fila,column=columna)

#Definimos una funcion que crea titulos para las tablas
def crear_titulo(contenedor,texto, columna, fila, ancho):
    label = tk.Label(contenedor,text=texto,bg="#181624", fg="#F5F5F5" ,pady=15, width=ancho)
    label.grid(row=fila,column=columna)

#Definimos una funcion que desaparezca la pantalla inicial y active el menu de gestion de clientes
def cambio_ventana2():
    contenedor.place_forget()
    Contenedor_botones.place_forget()
    Contenedor_buscador.place(x=500,y=190)
    Contenedor_lista_clientes.place(x=10,y=190)
    Respuesta.place(x=500,y=300)
    Agregar_cliente.place(x=500,y=600)

#Definimos una funcion que ejecute el buscador
def pulsar_buscar_cliente():
    for widget in Respuesta.winfo_children():
        widget.destroy()
    email_ingresado = Buscador.get()
    buscar_cliente(email_ingresado)

#Definimos una funcion que desaparece el menu de gestion de clientes y activa el menu de añadir clientes
def cambio_ventana3():
    Contenedor_buscador.place_forget()
    Contenedor_lista_clientes.place_forget()
    Respuesta.place_forget()
    Agregar_cliente.place_forget()

####################################################################################################################################

################################ En esta zona iran los atributos de la ventana que vallamos creando ################################

#Transformamos las imagenes elegidas en fondos para las ventanas
Fondo_inicial = PhotoImage(file = "fondo_inicio.png")
Fondo_1 = PhotoImage(file = "Ventana1.png")

#Creamos las tipografias especificas para las diversas partes del programa
Fuente_botones = font.Font(family = "Fragment Core", size=50)
Fuente_botones2 = font.Font(family = "Fragment Core", size=30)
Fuente_datos_presentacion = font.Font(family = "Times New Roman", size=40)
Fuente_titulo_biblioteca = font.Font(family = "Letter ^  Blocks", size=40)
Fuente_boton_cerrar = font.Font(family = "Fragment Core", size=53)
Fuente_titulo_biblioteca2 = font.Font(family = "Letter ^  Blocks", size=45)

#Creamos el marco donde almacenaremos la pantalla de inicio del programa
Menu_inicial = tk.Frame(bdd)
Menu_inicial.place(x=0,y=0,relheight=1,relwidth=1)

#Creamos un label que contenga como fondo la imagen que asignamos para el menu
Fondo_menu_inicial = tk.Label(Menu_inicial, image = Fondo_inicial)
Fondo_menu_inicial.place(x=0,y=0,relwidth=1,relheight=1)

#Creamos un label donde pondremos el nombre de la biblioteca
Titulo_biblioteca = tk.Label(Menu_inicial, text = "El Palacio Del Conocimiento", font = Fuente_titulo_biblioteca, bg = "#E8BBE9")
Titulo_biblioteca.place(x=50,y=50)

#Creamos un boton a traves del cual accederemos al programa
Boton_empezar = tk.Button(Menu_inicial, text = "Acceder", font = Fuente_botones, command = cambio_ventana1 ,bg = "#C2A5E9")
Boton_empezar.place(x=150,y=300)

#Creamos un boton que nos permita cerrar la ventana
Boton_cerrar = tk.Button(Menu_inicial, text="Cerrar Ventana", font = Fuente_botones ,command = cerrar_bdd ,bg ="#F5F5F5")
Boton_cerrar.place(x=50,y=600)

#Creamos un label donde ira el nombre del creador del programa
Creador = tk.Label(Menu_inicial, text = "Nicolas Luna\nIngenieria en Sistemas\nSegundo Semestre", font = Fuente_datos_presentacion , bg = "#564E87")
Creador.place(x=1050,y=625)

#Creamos un segundo marco donde se contendra la interfaz principal de la biblioteca para
Ventana_1 = tk.Frame(bdd)

#Creamos un label para el fondo de esta ventana
Fondo_ventana_1 = tk.Label(Ventana_1, image=Fondo_1)
Fondo_ventana_1.place(x=0, y=0,relheight=1,relwidth=1)

#Creamos un label donde ira el nombre de la biblioteca
Titulo_biblioteca2 = tk.Label(Ventana_1, text="El Palacio Del Conocimiento", font=Fuente_titulo_biblioteca2, bg="#C2A5E9")
Titulo_biblioteca2.place(x=40,y=50)

#Creamos los labels y el frame que nos serviran como contenedores para los datos
contenedor = tk.Frame(Ventana_1, bg="#181624", pady=5,padx=5)
contenedor.place(x=10,y=180)
tabla_libros_disponibles(contenedor)

#Creamos un contenedor donde iran los botones de la interfaz
Contenedor_botones = tk.Frame(Ventana_1, bg="#F5F5F5", padx=5,pady=5)
Contenedor_botones.place(x=700, y=180)

#Creamos el boton que llevara a la pestaña de gestion de clientes
Boton_clientes = tk.Button(Contenedor_botones, bg="#564E87",text="Gestion de Clientes", font=Fuente_botones, command=cambio_ventana2)
Boton_clientes.grid(row=1,column=1)

#Creamos un separador para colocar el buscador
Contenedor_buscador = tk.Frame(Ventana_1, bg="#F5F5F5")

#Creamos una entrada de texto para crear el buscador
Buscador = tk.Entry(Contenedor_buscador, font=Fuente_botones, bg="#E8BBE9")
Buscador.grid(row=1,column=1)

#Creamos un boton que envie el texto ingresado al programa
Buscar = tk.Button(Contenedor_buscador, text="Buscar",font=Fuente_botones2, bg="#C2A5E9",height=1, command=pulsar_buscar_cliente)
Buscar.grid(row=1, column=2)

#Creamos un contenedor donde se inserte el cliente buscado
Respuesta = tk.Frame(Ventana_1, bg="#181624",padx=5,pady=5)

#Creamos un contenedor donde ira un boton para insertar nuevos clientes
Agregar_cliente = tk.Frame(Ventana_1, bg="#F5F5F5",padx=5,pady=5)

#Creamos un boton para insertar nuevos clientes
Boton_agregar_cliente = tk.Button(Agregar_cliente, bg="#C2A5E9", text="Agregar nuevo Cliente", font=Fuente_botones, command=cambio_ventana3)
Boton_agregar_cliente.pack()

#Creamos un contenedor donde se van a colocar las listas de clientes
Contenedor_lista_clientes = tk.Frame(Ventana_1, bg="#181624")
tabla_clientes_existentes(Contenedor_lista_clientes)

#Creamos un contenedor que haga de separador entre los botones
Separador1 = tk.Frame(Contenedor_botones, bg="#F5F5F5", height=75)
Separador1.grid(row=2,column=1)

#Creamos el boton que llevara a la pestaña de gestion de prestamos
Boton_prestamos = tk.Button(Contenedor_botones, bg="#564E87",text="Gestion de Prestamos", font=Fuente_botones)
Boton_prestamos.grid(row=3,column=1)

#Creamos un contenedor que haga de separador entre los botones
Separador2 = tk.Frame(Contenedor_botones, bg="#F5F5F5", height=75)
Separador2.grid(row=4,column=1)

#Creamos el boton que llevara a la pestaña de recibir libros
Boton_prestamos = tk.Button(Contenedor_botones, bg="#564E87",text="Recibir Libros", font=Fuente_botones)
Boton_prestamos.grid(row=5,column=1)

#Creamos un boton con el que podamos cerrar la ventana
Boton_cerrar2 = tk.Button(Ventana_1, text="X", font=Fuente_boton_cerrar, command=cerrar_bdd, bg="red2")
Boton_cerrar2.place(x=1423, y=0)

####################################################################################################################################

#Usamos el metodo mainloop para que al ejecutar el codigo la ventana sea visible
bdd.mainloop()
################################ En esta zona hacemos la peticion al sql de los libros que esten prestados ################################
'''
En la base de datos llamada "Biblioteca" en la que hay una tabla con le nombre 
"Libro" extraigo todas la filas que tengan en la columna "Libro_estado" un numero distinto de 1, 
el resultado deves meterlo en un areglo "

# Crear un cursor para interactuar con la base de datos
cursor = conn.cursor()

# Consulta SQL para extraer filas con Libro_estado distinto de 1
Consulta_libros_prestados = "SELECT * FROM Libro WHERE Libro_estado <> 1"

# Ejecutar la consulta
cursor.execute(Consulta_libros_prestados)

# Inicializar una lista para almacenar los resultados
Resultado = []

# Recorrer las filas resultantes y agregarlas al arreglo
for row in cursor:
    # Convertir los valores numéricos a cadenas antes de agregarlos
    Convertir_values = [str(value) if isinstance(value, int) or isinstance(value, float) else value for value in row]
    Resultado.append(Convertir_values)

# Cerrar el cursor y la conexión a la base de datos
cursor.close()
conn.close()

# Verificar si se encontraron resultados
if Resultado:
    # Imprimir los resultados formateados
    for Resultado in Resultado:
        Resultado_str = [str(value) for value in Resultado]
        print(Resultado_str)
else:
    print("No se encontraron resultados")

'''