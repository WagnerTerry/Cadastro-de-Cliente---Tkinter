from tkinter import *
from tkinter import ttk
root = Tk()

l = ttk.Label(root, text="Começando...")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text="Movido o mouse \n"
                                        "para dentro"))
l.bind('<Leave>', lambda e: l.configure(text="Movido o mouse \n"
                                        "para fora"))
l.bind('<1>', lambda e: l.configure(text="Clicou botão esquerdo do mouse"))
l.bind("<Double-1>", lambda e: l.configure(text="Duplo Clique"))
l.bind("<B3-Motion>", lambda e: l.configure(text="Arraste o botão \n"
                                          "direito para %d, %d" % (e.x, e.y)))

root.mainloop()