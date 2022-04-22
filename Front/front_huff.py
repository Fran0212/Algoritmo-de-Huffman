
from Back.back_huff import *
# biblioteca pela interface
from tkinter import filedialog as dlg
from tkinter import *
from tkinter import messagebox

# importa o erro para o tratamento
from configparser import NoSectionError


def compactar():
   try:
      arquivo_loc = dlg.askopenfilename(title="select a file", filetypes=(("txt files", "*.txt"), ("All files", "*")))
      erro_import(arquivo_loc, "c")
   except ImportError:
      messagebox.showerror(title="Error", message="Extensão inválida, selecione um arquivo .txt")
   else:
      try:
         semi_compac(arquivo_loc)
      except:
         messagebox.showerror(title="Error", message="Ops, algo deu errado!")
      else:
         messagebox.showinfo(title="Sucesso", message="Arquivo compactado com sucesso!")


def descompactar():
   try:
      arquivo_loc = dlg.askopenfilename(title="select a file", filetypes=(("huff files", "*.huff"), ("All files", "*")))
      erro_import(arquivo_loc, "x")
   except ImportError:
      messagebox.showerror(title="Error", message="Extensão inválida, selecione um arquivo .huff")
   else:
      cp.read('save.ini', encoding="utf-8")

      try:
         nome_section = arquivo_loc.lower()
         formate = cp[nome_section].get("tipo_formato")
         desc(nome_section, formate)

      except NoSectionError:
         messagebox.showerror(title="Error", message="Ops, algo deu errado!")

      else:
         messagebox.showinfo(title="Sucesso", message="Arquivo compactado com sucesso!")


def reconstruir():
   try:
      arquivo_loc = dlg.askopenfilename(title="select a file", filetypes=(("huff files", "*.huff"), ("All files", "*")))
      erro_import(arquivo_loc, "r")
   except ImportError:
      messagebox.showerror(title="Error", message="Extensão inválida, selecione um arquivo .huff")
   else:
      cp.read('save.ini', encoding="utf-8")

      try:
         nome_section = arquivo_loc.lower()
         formate = cp[nome_section].get("tipo_formato")
         desc(nome_section, formate)

      except NoSectionError:
         messagebox.showerror(title="Error", message="Ops, algo deu errado!")
      else:
         messagebox.showinfo(title="Sucesso", message="Arquivo reconstruido com sucesso!")

