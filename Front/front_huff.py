
from Back.back_huff import *
# biblioteca pela interface
from tkinter import filedialog as dlg
from tkinter import *
from tkinter import messagebox

# importa o erro para o tratamento
from configparser import NoSectionError


def compactar():
   arquivo_loc = dlg.askopenfilename(title="select a file", filetypes=(("text files", "*.txt"), ("All files", "*")))

   try:
      semi_compac(arquivo_loc)
   except:
      messagebox.showerror(title="Error", message="Ops, algo deu errado!")
   else:
      messagebox.showinfo(title="Sucesso", message="Arquivo compactado com sucesso!")


def descompactar():
   arquivo_loc = dlg.askopenfilename(title="select a file", filetypes=(("huff files", "*.huff"), ("All files", "*")))

   cp.read('save.ini', encoding="utf-8")

   try:
      nome_section = arquivo_loc.lower()
      formate = cp[nome_section].get("tipo_formato")
      desc(nome_section, formate)

   except NoSectionError:
      messagebox.showerror(title="Error", message="Ops, algo deu errado!")

   else:
      messagebox.showinfo(title="Sucesso", message="Arquivo compactado com sucesso!")