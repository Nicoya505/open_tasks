import tkinter as tk
from tkinter import ttk


class Frame(tk.Frame):
    def __init__(self, root ):
        super().__init__(root)
        self.root = root
        self.pack()
        
        self.initialComponent()
        self.show_table()
        
    
    
    def initialComponent(self):
        
        # Label
        self.lbl_title = tk.Label(self, text="Title: ")
        self.lbl_title.config(font=("Arial", 12, "bold"))
        self.lbl_title.grid(row=0, column=0, padx=10, pady=10)
        
        self.lbl_description = tk.Label(self, text="Description: ")
        self.lbl_description.config(font=("Arial", 12, "bold"))
        self.lbl_description.grid(row=1, column=0, padx=10, pady=10)
        
        # Entrys
        self.svar_title = tk.StringVar()
        self.etr_title = tk.Entry(self, textvariable=self.svar_title)
        self.etr_title.config(width=50, font=("Arial", 12))
        self.etr_title.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        
        self.svar_description = tk.StringVar()
        self.etr_description = tk.Entry(self, textvariable=self.svar_description)
        self.etr_description.config(width=50, font=("Arial", 12))
        self.etr_description.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        
        # Buttoms
        
        self.btn_new = tk.Button(self, text="New")
        self.btn_new.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#158645",
            cursor="hand2",
            activebackground="#35BD6F"
        )
        self.btn_new.grid(row=2, column=0, padx=10, pady=10)
        
        self.btn_save = tk.Button(self, text="Save")
        self.btn_save.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#1658A2",
            cursor="hand2",
            activebackground="#3586DF"
        )
        self.btn_save.grid(row=2, column=1, padx=10, pady=10)
        
        self.btn_cancel = tk.Button(self, text="Cancel")
        self.btn_cancel.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#BD152E",
            cursor="hand2",
            activebackground="#E15370"
        )
        self.btn_cancel.grid(row=2, column=2, padx=10, pady=10)
        
    
    def show_table(self):
        self.table = ttk.Treeview(self, columns=("Title", "Description", "Status"))
        self.table.grid(row=3, column=0, columnspan=4, sticky="nse" )
        
        self.scroll = ttk.Scrollbar(self,
                                    orient="vertical",
                                    command=self.table.yview
                                    )
        self.scroll.grid(row=3, column=4, sticky="nse")
        self.table.configure(yscrollcommand=self.scroll.set)
        
        self.table.heading("#0", text="ID")
        self.table.heading("#1", text="TITLE")
        self.table.heading("#2", text="DESCRIPTION")
        self.table.heading("#3", text="STATUS")
        
        self.table.insert("",
                          0,
                          text="1",
                          values= ("Programar", "importante", "pending")
                          )
        
        self.btn_update = tk.Button(self, text="Update")
        self.btn_update.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#158645",
            cursor="hand2",
            activebackground="#35BD6F"
        )
        self.btn_update.grid(row=4, column=0, padx=10, pady=10)
        
        self.btn_status = tk.Button(self, text="change status")
        self.btn_status.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#1658A2",
            cursor="hand2",
            activebackground="#3586DF"
        )
        self.btn_status.grid(row=4, column=1, padx=10, pady=10)
        
        self.btn_delete = tk.Button(self, text="Delete")
        self.btn_delete.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#BD152E",
            cursor="hand2",
            activebackground="#E15370"
        )
        self.btn_delete.grid(row=4, column=2, padx=10, pady=10)