from config import engine, Base

from views import Frame
from views import menu_bar

import tkinter as tk

def main():
    Base.metadata.create_all(engine)
    
    root = tk.Tk()
    root.title("Open Tasks")
    root.resizable(0,0)
    
    menu_bar(root)
    
    app = Frame(root)
    
    app.mainloop()
    
    
if __name__ == "__main__":
    main()