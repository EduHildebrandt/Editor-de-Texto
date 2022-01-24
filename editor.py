from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = "" #La vamos a utilizar para almacenar la ruta del archivo

def nuevo():
    global ruta
    mensaje.set("Nuevo Archivo")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Editor de TEXTOOOO")

def abrir():
    global ruta
    mensaje.set("Abrir Archivo")
    ruta = FileDialog.askopenfilename(initialdir='.', filetypes=(("Archivos de texto", ".txt"),), title="Abrir archivos de texto")

    if ruta != "":
        archivo = open(ruta, 'r')
        contenido = archivo.read()
        texto.delete(1.0, 'end')
        texto.insert('insert', contenido)
        archivo.close()
        root.title(ruta + " - Editor de TEXTO")

def guardar():
    global ruta
    mensaje.set("Guardar Archivo")
    if ruta != "":
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El Archivo se ha guardado con exito")
    else:
        guardar_como()


def guardar_como():
    global rura
    mensaje.set("Guardar Archivo como...")
    fichero = FileDialog.asksaveasfile(title="Guardar Archivo", mode='w', defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El Archivo se ha guardado con exito")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""

#Configuración de la raiz
root = Tk()
root.title("Editor de TEXTO")


#Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como...", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

#caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

#Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor")
monitor = Label(root, textvariable=mensaje, justify='left')
monitor.pack(side='left')

root.config(menu=menubar)
#Finalmente el bucle de la aplicación
root.mainloop()