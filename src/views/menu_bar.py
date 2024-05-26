import tkinter as tk

def menu_bar(root):
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar, width=500, height=600)
    
    start_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu= start_menu)

    start_menu.add_command(label="Exit", command=root.destroy)
    
    