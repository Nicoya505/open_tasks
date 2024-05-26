from services import TaskServices
from models import TaskModel

from config import Session

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Frame(tk.Frame):
    def __init__(self, root ):
        super().__init__(root)
        self.root = root
        self.pack()
        
        self.id_pelicula = None
        self.initialComponent()
        self.show_table()
        self.disable_fields()
        
    
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
        
        self.btn_new = tk.Button(self, text="New", command=self.enable_fields)
        self.btn_new.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#158645",
            cursor="hand2",
            activebackground="#35BD6F"
        )
        self.btn_new.grid(row=2, column=0, padx=10, pady=10)
        
        self.btn_save = tk.Button(self, text="Save", command=self.create_Task)
        self.btn_save.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#1658A2",
            cursor="hand2",
            activebackground="#3586DF"
        )
        self.btn_save.grid(row=2, column=1, padx=10, pady=10)
        
        self.btn_cancel = tk.Button(self, text="Cancel", command=self.disable_fields)
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
        session = Session()
        
        tasks = TaskServices(session).get_tasks()
        tasks.reverse()
        
        self.table = ttk.Treeview(self, columns=("Title", "Description", "Status"))
        self.table.grid(row=3, column=0, columnspan=4, sticky="nse" )
        
        self.scroll = ttk.Scrollbar(self,
                                    orient="vertical",
                                    command=self.table.yview
                                    )
        self.scroll.grid(row=3,
                         column=4,
                         sticky="nse"
                         )
        
        self.table.configure(yscrollcommand=self.scroll.set)
        
        self.table.heading("#0", text="ID")
        self.table.heading("#1", text="TITLE")
        self.table.heading("#2", text="DESCRIPTION")
        self.table.heading("#3", text="STATUS")
        
        for task in tasks:
            self.table.insert("",
                          0,
                          text=task.id,
                          values=(
                              task.title,
                              task.description,
                              task.status
                          )
            )
        
        self.btn_update = tk.Button(self, text="Update", command=self.update_task)
        self.btn_update.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#158645",
            cursor="hand2",
            activebackground="#35BD6F"
        )
        self.btn_update.grid(row=4, column=0, padx=10, pady=10)
        
        self.btn_status = tk.Button(self, text="change status", command=self.change_status)
        self.btn_status.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#1658A2",
            cursor="hand2",
            activebackground="#3586DF"
        )
        self.btn_status.grid(row=4, column=1, padx=10, pady=10)
        
        self.btn_delete = tk.Button(self, text="Delete", command=self.delete_task)
        self.btn_delete.config(
            width=20,
            font=("Arial", 12, "bold"),
            fg="#DAD5D6",
            bg="#BD152E",
            cursor="hand2",
            activebackground="#E15370"
        )
        self.btn_delete.grid(row=4, column=2, padx=10, pady=10)
    
    
    def enable_fields(self):
        self.btn_save.config(state="normal")
        self.btn_cancel.config(state="normal")
        self.btn_update.config(state="normal")
        self.btn_delete.config(state="normal")
        self.btn_status.config(state="normal")
        self.btn_new.config(state="disabled")
        
        self.etr_title.config(state="normal")
        self.etr_description.config(state="normal")
    
    
    def disable_fields(self):
        
        self.id_pelicula = None
        
        self.svar_title.set("")
        self.svar_description.set("")
        
        self.btn_save.config(state="disabled")
        self.btn_cancel.config(state="disabled")
        self.btn_new.config(state="normal")
        
        self.etr_title.config(state="disabled")
        self.etr_description.config(state="disabled")
        
    
    def create_Task(self):
        
        session = Session()
        
        task = TaskModel(
            title = self.etr_title.get(),
            description = self.etr_description.get()
        )
        
        if self.id_pelicula == None:
            TaskServices(session).create_task(task)
        else:
            TaskServices(session).update_task(task, self.id_pelicula)
        
        self.disable_fields()
        self.show_table()
        
    
    def update_task(self):
        
        try:
            
            self.id_pelicula = self.table.item(self.table.selection())['text']
            title = self.table.item(self.table.selection())["values"][0]
            description = self.table.item(self.table.selection())["values"][1]
            
            self.enable_fields()
            self.etr_title.insert(0, title)
            self.etr_description.insert(0, description)
        except:
            messagebox.showwarning("Data editing", "No record has been selected")
        
    
    def delete_task(self):
        
            session = Session()
            self.id_pelicula = self.table.item(self.table.selection())['text']
            
            if not self.id_pelicula:
                messagebox.showwarning("Delete data", "No record has been selected")
                
            TaskServices(session).delete_task(self.id_pelicula)        

            self.show_table()
            self.id_pelicula = None
            
    
    def change_status(self):
        session = Session()
        self.id_pelicula = self.table.item(self.table.selection())['text']
        
        if self.id_pelicula:
            status = self.table.item(self.table.selection())["values"][2]
            
            new_status = "pending" if status == "completed" else "completed"
            
            TaskServices(session).change_status_task(new_status, self.id_pelicula)        

            self.show_table()
            self.id_pelicula = None
            
            return 
            
            
        messagebox.showwarning("Change status", "No record has been selected")
        
            
            
            