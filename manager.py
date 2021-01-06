from tkinter import *
from tkinter import Tk,Label,Button,Frame,simpledialog,Image 

from tkinter import Menu
import os
import subprocess

home=os.getcwd()

window = Tk()

window.title("App Manager de Mantenimiento")
window.geometry('800x600')
frame=Frame(window,bg="#212F3C")


menu = Menu(window)
'''
new_item = Menu(menu)

new_item.add_command(label='New')

new_item.add_separator()

new_item.add_command(label='Edit')
'''


def clicked1():

     #os.system('sudo gnome-terminal "./clearRAM.sh" ')
     os.system("gnome-terminal -e 'bash -c \"sudo ./clearRAM.sh; exec bash\"'")       
     lbl.configure(text="Limpiar RAM !!")
     

btn1 = Button(window, text="1.-Limpiar RAM",bg="#27AE60",fg="white",padx=10,pady=10,activebackground="#1F618D",activeforeground="white",command=clicked1)

btn1.grid(row=3,sticky=W,pady=5)


def clicked2():

    
    os.system("gnome-terminal -e 'bash -c \"sudo ./limpiar_cache_chrome.sh; exec bash\"'")    
    lbl.configure(text="Limpiar Cache del Chrome !!")

btn2 = Button(window, text="2.-Limpiar Cache del Chrome",bg="#C0392B",fg="white",padx=10,pady=10,activebackground="#1F618D",activeforeground="white", command=clicked2)

btn2.grid(row=6,sticky=W,pady=5)


def clicked3():

     
    os.system("gnome-terminal -e 'bash -c \"sudo ./ubucleaner; exec bash\"'")  
    lbl.configure(text="Limpieza General !!")

btn3 = Button(window, text="3.-Limpieza General",bg="#27AE60",fg="white",padx=10,pady=10,activebackground="#1F618D",activeforeground="white" ,command=clicked3)

btn3.grid(row=9,sticky=W,pady=5)


def clicked4():

    
    os.system("gnome-terminal -e 'bash -c \"sudo ./update-limpieza.sh; exec bash\"'")  
    lbl.configure(text="Update del Sistema !!")

btn4 = Button(window, text="4.-Update del Sistema",bg="#C0392B",fg="white",padx=10,pady=10,activebackground="#1F618D",activeforeground="white" ,command=clicked4)

btn4.grid(row=12,sticky=W,pady=5)

def clicked5():

    
    os.system("gnome-terminal -e 'bash -c \"sudo ./Stacer-x86_64.AppImage; exec bash\"'")  
    lbl.configure(text="Stacer !!")

btn5 = Button(window, text="5.-Stacer",bg="#27AE60",fg="white",padx=10,pady=10,activebackground="#1F618D",activeforeground="white" ,command=clicked5)

btn5.grid(row=15,sticky=W,pady=5)


def clicked6():

    
    #window.destroy()
    os.system("gnome-terminal -e 'bash -c \"sudo ./emptycrashes.sh; exec bash\"'")  
    lbl.configure(text="Vaciar Crashes !!")

btn6 = Button(window, text="6.-Vaciar Crashes",bg="#C0392B",fg="white",padx=10,pady=10,activebackground="#1F618D",activeforeground="white", command=clicked6)

btn6.grid(row=18,sticky=W,pady=5)

'''
menu.add_command(label='1.-Limpiar RAM') 
menu.add_cascade(label='2.-Limpiar Cache del Chrome')
menu.add_cascade(label='3.-Limpieza General')
menu.add_cascade(label='4.-Update del Sistema')
menu.add_cascade(label='5.-Stacer')
menu.add_cascade(label='6.-Salir')

window.config(menu=menu)
 '''

#menu = Menu(window)
filemenu = Menu(menu, tearoff=0)
filemenu.add_command(label="1.-Limpiar RAM", command=clicked1)
filemenu.add_command(label="2.-Limpiar Cache del Chrome", command=clicked2)
filemenu.add_command(label="3.-Limpieza General", command=clicked3)
filemenu.add_command(label="4.-Update del Sistema", command=clicked4)
filemenu.add_command(label="5.-Stacer", command=clicked5)
filemenu.add_command(label="6.-Vaciar crashes", command=clicked6)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menu.add_cascade(label="Opciones", menu=filemenu)
window.config(menu=menu)

lbl = Label(window, text="")

lbl.grid(column=0, row=0) 


window.mainloop()