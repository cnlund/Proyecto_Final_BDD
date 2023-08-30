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

####################################################################################################################################

############################## En esta zona iran los comandos de los botones que vallamos a utilizar ###############################

#definimos una funcion que cuando se pulse ese boton destruya la ventana
def cerrar_bdd():
    bdd.destroy()

####################################################################################################################################

################################ En esta zona iran los atributos de la ventana que vallamos creando ################################

#Transformamos las imagenes elegidas en fondos para las ventanas
Fondo_inicial = PhotoImage(file = "fondo_inicio.png")

#Creamos las tipografias especificas para las diversas partes del programa
Fuente_botones = font.Font(family = "Fragment Core", size=50)
Fuente_creador = font.Font(family = "Times New Roman", size=70)
Fuente_titulo_biblioteca = font.Font(family = "Letter ^  Blocks", size=40)

#Creamos el marco donde almacenaremos la pantalla de inicio del programa
Menu_inicial = tk.Frame(bdd)
Menu_inicial.place(x=0,y=0,relheight=1,relwidth=1)

#Creamos un label que contenga como fondo la imagen que asignamos para el menu
Fondo_menu_inicial = tk.Label(Menu_inicial, image = Fondo_inicial)
Fondo_menu_inicial.place(x=0,y=0,relwidth=1,relheight=1)

#Creamos un label donde pondremos el nombre de la biblioteca
Titulo_biblioteca = tk.Label(Menu_inicial, text = "El Palacio Del Conocimiento", font = Fuente_titulo_biblioteca, bg = "Magenta4")
Titulo_biblioteca.place(x=50,y=50)

#Creamos un boton que nos permita cerrar la ventana
Boton_cerrar = tk.Button(Menu_inicial, text="Cerrar Ventana", font = Fuente_botones ,command = cerrar_bdd ,bg ="HotPink3")
Boton_cerrar.place(x=50,y=600)

#Creamos un label donde ira el nombre del creador del programa
Creador = tk.Label(Menu_inicial, text = "Creado por Nicolas Luna.", font = Fuente_creador, bg = "RoyalBlue4")
Creador.place(x=575,y=775)

####################################################################################################################################

#Usamos el metodo mainloop para que al ejecutar el codigo la ventana sea visible
bdd.mainloop()