from config import engine, Base

from views import Frame

import tkinter as tk

def main():
    Base.metadata.create_all(engine)
    
    root = tk.Tk()
    root.title("Open Tasks")
    root.resizable(0,0)
    
    app = Frame(root)
    
    app.mainloop()
    
    
    
    

if __name__ == "__main__":
    main()