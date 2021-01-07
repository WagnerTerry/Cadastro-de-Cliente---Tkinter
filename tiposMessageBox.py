from tkinter import *
from tkinter import messagebox

root = Tk()

def display():
    messagebox.showinfo("Info", "Só pra voce saber")
    messagebox.showwarning("Perigo", "Melhor ter cuidado")
    messagebox.showerror("Erro", "Algo deu errado")

    okcancel = messagebox.askokcancel("O que voce acha?", "Devemos ir em frente?")
    print(okcancel)

    yesno = messagebox.askyesno("O que vc acha?", "Por favor decida")
    print(yesno)

    retryCancel = messagebox.askretrycancel("O que vc acha?", "Qual a sua resposta")
    print(retryCancel)

    answer = messagebox.askquestion("O que vc acha?", "Por favor decida")

b1 = Button(root, text="Exibir dialogos", command = display)
b1.pack()

root.mainloop()