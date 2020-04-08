from tkinter import *
import sqlite3
from tkinter import messagebox

#*********************** GLOBALES ***************************
root = Tk()
id_ = StringVar()
nombre = StringVar()
password = StringVar()
apellido = StringVar()
direccion = StringVar()


#********************** FUNCIONES ***************************
#------------------------- funciones bbdd -------------------
def conectar():
	try:
		conexion = sqlite3.connect("base")
		cursor = conexion.cursor()
		cursor.execute('''
			CREATE TABLE usuarios (
			ID integer PRIMARY KEY AUTOINCREMENT,
			NOMBRE varchar(50),
			CONTRASEÑA varchar(50),
			APELLIDO varchar(50),
			DIRECCION varchar(50),
			COMENTARIO varchar(100)) 
		''')
		conexion.commit()
		conexion.close()
		messagebox.showinfo("Confirmacion","base de datos creada")
	except sqlite3.OperationalError as e:
		messagebox.showwarning("Operacion incorrecta","base de datos existente")
#-----------------------------------------------------------------------------------------------
def salir():
	valor=messagebox.askquestion("Mensaje de confirmación","Deseas salir de la aplicacion?")
	if valor=="yes":
		root.destroy()
#-------------------------------- FUNCIONES DE BORRAR -----------------------------------------
def borrar():
	id_entry.delete(0,END)
	nombre_entry.delete(0,END)
	password_entry.delete(0,END)
	apellido_entry.delete(0,END)
	direccion_entry.delete(0,END)
	comentario_text.delete(1.0,END)

#********************************** FUNCIONES DE CRUD ************************************
#------------------------------------- CREATE ------------------------------------------
def create():
	comentario = comentario_text.get(1.0,END)
	conexion = sqlite3.connect("base")
	cursor = conexion.cursor()
	cursor.execute("INSERT INTO usuarios (ID,NOMBRE,CONTRASEÑA,APELLIDO,DIRECCION,COMENTARIO) VALUES(NULL,?,?,?,?,?)",(nombre.get(),password.get(),apellido.get(),direccion.get(),comentario))
	messagebox.showinfo("Confirmacion","registro insertado")
	conexion.commit()
	conexion.close()
#------------------------------------- READ --------------------------------------------
def read():
	conexion = sqlite3.connect("base")
	cursor = conexion.cursor()
	cursor.execute("SELECT * FROM usuarios WHERE ID='id_'")
	usuarios_lista = cursor.fetchall()
	print(usuarios_lista)
	conexion.commit()
	conexion.close()
#------------------------------------- UPDATE ------------------------------------------
#------------------------------------- DELETE ------------------------------------------



#********************************** CREACION DEL MENU ************************************
menubar = Menu(root)
root.config(menu=menubar)
menu_bbdd=Menu(menubar,tearoff=0)
menu_bbdd.add_command(label="conectar",command=conectar)
menu_bbdd.add_command(label="salir",command=salir)

menu_borrar=Menu(menubar,tearoff=0)
menu_borrar.add_command(label="borrar campos",command=borrar)

menu_crud=Menu(menubar,tearoff=0)
menu_crud.add_command(label="create",command=create)
menu_crud.add_command(label="read",command=read)
menu_crud.add_command(label="update")
menu_crud.add_command(label="delete")

menu_ayuda=Menu(menubar,tearoff=0)
menu_ayuda.add_command(label="licencia")
menu_ayuda.add_command(label="acerca de ...")
#---------------------- agregando ---------------------------
menubar.add_cascade(label="BBDD",menu=menu_bbdd)
menubar.add_cascade(label="borrar",menu=menu_borrar)
menubar.add_cascade(label="CRUD",menu=menu_crud)
menubar.add_cascade(label="ayuda",menu=menu_ayuda)

#******************* CREACION EN EL FRAME *******************
frame=Frame(root)
frame.pack()
#---------------------- LABEL ------------------------------
id_label = Label(frame,text="id",padx=1,pady=10)
id_label.grid(row=0,column=0)
nombre_label = Label(frame,text="nombre",padx=1,pady=10,justify="center")
nombre_label.grid(row=1,column=0)
password_label = Label(frame,text="contraseña",padx=1,pady=10,justify="center")
password_label.grid(row=2,column=0)
apellido_label = Label(frame,text="apellido",padx=1,pady=10,justify="center")
apellido_label.grid(row=3,column=0)
direccion_label = Label(frame,text="direccion",padx=1,pady=10,justify="center")
direccion_label.grid(row=4,column=0)
comentario_label = Label(frame,text="comentario",padx=1,pady=10,justify="center")
comentario_label.grid(row=5,column=0)
#--------------------- Entry -------------------------------
id_entry=Entry(frame,textvariable=id_)
id_entry.grid(row=0,column=1,padx=15,pady=10,columnspan=3)
nombre_entry=Entry(frame,justify="right",fg="red",textvariable=nombre)
nombre_entry.grid(row=1,column=1,padx=10,pady=10,columnspan=3)
password_entry=Entry(frame,show="*",textvariable=password)
password_entry.grid(row=2,column=1,padx=10,pady=10,columnspan=3)
apellido_entry=Entry(frame,textvariable=apellido)
apellido_entry.grid(row=3,column=1,padx=10,pady=10,columnspan=3)
direccion_entry=Entry(frame,textvariable=direccion)
direccion_entry.grid(row=4,column=1,padx=10,pady=10,columnspan=3)
#------------------------- text y scroll-----------------------
comentario_text = Text(frame,width=15,height=4)
comentario_text.grid(row=5,column=1,padx=10,columnspan=3)
comentario_scroll = Scrollbar(frame,command=comentario_text.yview)
comentario_scroll.grid(row=5,column=4,sticky="nsew")
comentario_text.config(yscrollcommand=comentario_scroll.set)
#------------------------- botones ----------------------------
create_button = Button(frame,text="create")
create_button.grid(row=6,column=0,pady=10)
read_button = Button(frame,text=" read ")
read_button.grid(row=6,column=1,pady=10)
update_button = Button(frame,text="update")
update_button.grid(row=6,column=2,padx=10)
delete_button = Button(frame,text="delete")
delete_button.grid(row=6,column=3)
#************************** CIERRES ***************************

root.mainloop()