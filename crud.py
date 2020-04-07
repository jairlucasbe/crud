from tkinter import *
root = Tk()
#**************** CREACION DEL MENU *************************
menubar = Menu(root)
root.config(menu=menubar)
menu_bbdd=Menu(menubar,tearoff=0)
menu_bbdd.add_command(label="conectar")
menu_bbdd.add_command(label="salir")

menu_borrar=Menu(menubar,tearoff=0)
menu_borrar.add_command(label="borrar campos")

menu_crud=Menu(menubar,tearoff=0)
menu_crud.add_command(label="create")
menu_crud.add_command(label="read")
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
id_label = Label(frame,text="id",padx=1,pady=10,justify="center")
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
id_entry=Entry(frame)
id_entry.grid(row=0,column=1,padx=15,pady=10,columnspan=3)
nombre_entry=Entry(frame)
nombre_entry.grid(row=1,column=1,padx=10,pady=10,columnspan=3)
password_entry=Entry(frame)
password_entry.grid(row=2,column=1,padx=10,pady=10,columnspan=3)
apellido_entry=Entry(frame)
apellido_entry.grid(row=3,column=1,padx=10,pady=10,columnspan=3)
direccion_entry=Entry(frame)
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






root.mainloop()