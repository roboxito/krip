import tkinter as tk
from tkinter import *
from tkinter import filedialog
import time
from tkinter import messagebox
import os, glob
from cryptography.fernet import Fernet
import stat
from tkinter import simpledialog

#Utileria para encriptar, desencriptar y visualizar cadenas o archivos de texto de forma visual y sencilla, multiplatadorma.
# En ubuntu 24.x
#$ sudo apt install python3-tk
#$ sudo apt install venv
#$ python3 -m venv krip
#$ cd krip
#$ source bin/activate
#$ pip install cryptography
#python krip.py

#key=Fernet.generate_key()
#print(key)
key=b'B69FxcWQKd5CCsaWTtxB4vkCiw3nZn09nSU3stgPqsg='
fernet=Fernet(key)
################## Credenciales ####################
version="Krip v1.0"
####################################################

class Application(tk.Frame):
   def __init__(self, master=None):        
      ob=Tk()
      #width and height with location setting
      ob.geometry('1000x500+0+0')
      tk.Frame.__init__(self,master)          
      self.grid(row=0,column=0,sticky=tk.N+tk.S+tk.E+tk.W)                      
      self.createWidgets()        

   def createWidgets(self):
      top=self.winfo_toplevel()
      top.rowconfigure(0,weight=1)
      top.columnconfigure(0,weight=1)
      self.rowconfigure(0,weight=1)
      self.columnconfigure(0,weight=1)
      self.aTxt=tk.Text(self)
      self.aTxt.grid(row=0,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
      menubar=Menu(self)
      top.config(menu=menubar)
      file_menu=Menu(menubar,tearoff=0)        
      file_menu.add_command(label='Buscar',command=self.buscar)        
      file_menu.add_separator()
      file_menu.add_command(label='Salir',command=self.quit)        
      menubar.add_cascade(label='Archivo',menu=file_menu,underline=0)
      help_menu=Menu(menubar,tearoff=0)        
      help_menu.add_command(label='Acerca de',command=self.acercade)
      util_menu=Menu(menubar,tearoff=0)        
      menubar.add_cascade(label='Utilerias',menu=util_menu,underline=0)
      menubar.add_cascade(label='Ayuda',menu=help_menu,underline=0)
      util_menu.add_command(label='Encriptar archivo',command=self.encrip)
      util_menu.add_command(label='Desencriptar archivo',command=self.desencrip)
      util_menu.add_command(label='Abrir archivo encriptado',command=self.abrirencrip)
      util_menu.add_separator()
      util_menu.add_command(label='Encriptar string',command=self.encrip_str)
      util_menu.add_command(label='Desencriptar string',command=self.desencrip_str)

   #def (self):

   def buscar(self):
      cad=simpledialog.askstring("Krip", "Buscar", parent=self)    
      countVar=tk.StringVar()        
      posi=self.aTxt.search(cad,"1.0",stopindex="end",count=countVar)
      print(cad+" en "+posi)
      self.aTxt.tag_configure("buscar",background="green")
      self.aTxt.tag_add("buscar",posi,"%s + %sc" % (posi,countVar.get()))      
      self.aTxt.mark_set("insert",posi)
      self.aTxt.see("insert")
      return(cad)

   def abrirencrip(self):
      self.limpia()
      filename= filedialog.askopenfilename(initialdir="c:\\",title="Seleccione archivo encriptado",filetypes=[("Archivos encriptados",".enc")])
      if(filename ==""): return
      payload="Archivo seleccionado "+filename+" \n"
      self.aTxt.insert(tk.END,payload)
      fileObj=open(filename,"rb")
      data=fileObj.read()
      desencriptado=fernet.decrypt (data)
      fileObj.close()      
      
      #nvoarch=os.path.splitext(filename)[0]
      #fileObj=open(nvoarch,"wb")
      #fileObj.write(desencriptado)
      #fileObj.close()

      self.aTxt.insert(tk.END,desencriptado)      
      self.aTxt.update_idletasks()
      self.aTxt.update()

      #os.chmod(nvoarch,stat.S_IREAD)
      #os.startfile (nvoarch)
      #time.sleep(1)
      #os.chmod(nvoarch,stat.S_IWRITE)
      #os.remove(nvoarch)

   def desencrip(self):
      self.limpia()
      filename= filedialog.askopenfilename(initialdir="c:\\",title="Seleccione archivo encriptado",filetypes=[("Archivos encriptados",".enc")])
      if(filename ==""): return
      payload="Archivo seleccionado "+filename+" \n"
      self.aTxt.insert(tk.END,payload)
      fileObj=open(filename,"rb")
      data=fileObj.read()
      desencriptado=fernet.decrypt (data)
      fileObj.close()
      #nvoarch=os.path.splitext(filename)[0]+".txt"
      nvoarch=os.path.splitext(filename)[0]
      fileObj=open(nvoarch,"wb")
      fileObj.write(desencriptado)
      fileObj.close()
      payload="Archivo desencriptado "+nvoarch+" \n"
      self.aTxt.insert(tk.END,payload)
      os.remove(filename)

   def encrip(self):
      self.limpia()
      filename= filedialog.askopenfilename(initialdir="c:\\",title="Seleccione archivo de texto",filetypes=[("Archivos de texto",".txt")])
      if(filename==""): return
      payload="Archivo seleccionado "+filename+" \n"
      self.aTxt.insert(tk.END,payload)
      fileObj=open(filename,"rb")
      try:
         data=fileObj.read()
         encriptado=fernet.encrypt(data)
         fileObj.close()
         #nvoarch=os.path.splitext(filename)[0]+".enc"
         nvoarch=filename+".enc"
         fileObj=open(nvoarch,"wb")
         fileObj.write(encriptado)
         fileObj.close()
         payload="Archivo encriptado "+nvoarch+" \n"
         self.aTxt.insert(tk.END,payload)
         os.remove(filename)
      except UnicodeDecodeError as e:
         fileObj.close()
         payload="Caracter invalido en posicion \n"+str(e)      
         self.aTxt.insert(tk.END,payload)

   def encrip_str(self):
      data=self.aTxt.get("1.0",tk.END)
      if (data==""): return
      encriptado=fernet.encrypt(data.encode())

      payload="\nEncriptado:\n"+encriptado.decode()+" \n"
      self.aTxt.insert(tk.END,payload)

   def desencrip_str(self):
      data=self.aTxt.get("1.0",tk.END)
      if (data==""): return
      desencriptado=fernet.decrypt(data.encode())

      payload="\nDesencriptado:\n"+desencriptado.decode()+" \n"
      self.aTxt.insert(tk.END,payload)

   def limpia(self):
      self.aTxt.delete( "1.0",tk.END)
      fecha=time.strftime("%Y %B %d %H:%M:%S")
      self.aTxt.insert(tk.END,fecha+"\n")
      self.update_idletasks()
      #time.sleep(1)

   def acercade(self):
      self.limpia()
      messagebox.showinfo("Acerca de","""Encriptador de archivos y cadenas
"""+version+""" 
Copyleft (C) 2022 Jorge Lopez
roboxito@gmail.com""")


app=Application()
app.master.title('Encriptador de archivos y cadenas (Krip)')
app.mainloop()
