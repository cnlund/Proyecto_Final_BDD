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

#creamos una funcion que imprima la lista de libros disponibles
def tabla_libros_disponibles():
    crear_titulo("Libros",2,1,18)
    crear_titulo("Disponibles",3,1,18)
    crear_lista("ID",1,2, 5)
    crear_lista("Titulo",2,2,18)
    crear_lista("Autor",3,2,18)
    crear_lista("Fecha de Publicacion",4,2,20)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Libro WHERE Libro.Libro_estado = 1")
    i=3
    for row in cursor:
        crear_lista(row.Libro_id,1, i, 5)
        crear_lista(row.Libro_titulo,2,i,18)
        crear_lista(row.Libro_autor,3,i,18)
        crear_lista(row.Libro_fecha_publicacion,4,i,20)
        i=i+1

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
def crear_lista(texto, columna, fila, ancho):
    label = tk.Label(Contenedor,text=texto,bg="#F5F5F5",pady=15, width=ancho)
    label.grid(row=fila,column=columna)

#Definimos una funcion que crea titulos para las tablas
def crear_titulo(texto, columna, fila, ancho):
    label = tk.Label(Contenedor,text=texto,bg="#181624", fg="#F5F5F5" ,pady=15, width=ancho)
    label.grid(row=fila,column=columna)

####################################################################################################################################

################################ En esta zona iran los atributos de la ventana que vallamos creando ################################

#Transformamos las imagenes elegidas en fondos para las ventanas
Fondo_inicial = PhotoImage(file = "fondo_inicio.png")
Fondo_1 = PhotoImage(file = "Ventana1.png")

#Creamos las tipografias especificas para las diversas partes del programa
Fuente_botones = font.Font(family = "Fragment Core", size=50)
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
Contenedor = tk.Frame(Ventana_1, bg="#181624", pady=5,padx=5)
Contenedor.place(x=10,y=180)
tabla_libros_disponibles()

#Creamos un contenedor donde iran los botones de la interfaz
Contenedor_botones = tk.Frame(Ventana_1, bg="#F5F5F5", padx=5,pady=5)
Contenedor_botones.place(x=700, y=180)

#Creamos el boton que llevara a la pestaña de gestion de clientes
Boton_clientes = tk.Button(Contenedor_botones, bg="#564E87",text="Gestion de Clientes", font=Fuente_botones)
Boton_clientes.pack()

#Creamos el boton que llevara a la pestaña de gestion de prestamos
Boton_prestamos = tk.Button(Contenedor_botones, bg="#564E87",text="Gestion de Prestamos", font=Fuente_botones)
Boton_prestamos.pack()

#Creamos un boton con el que podamos cerrar la ventana
Boton_cerrar2 = tk.Button(Ventana_1, text="X", font=Fuente_boton_cerrar, command=cerrar_bdd, bg="red2")
Boton_cerrar2.place(x=1423, y=0)

####################################################################################################################################

#Usamos el metodo mainloop para que al ejecutar el codigo la ventana sea visible
bdd.mainloop()