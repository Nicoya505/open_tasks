
from models import TaskModel

from tkinter import messagebox

class TaskServices:
    def __init__(self, session):
        self.session = session
    
    
    def create_task(self, task):
        try:
            self.session.add(task)
            self.session.commit()
        except:
            messagebox.showerror("Create Task", "The task could not be created")
        
        return
    
    
    def get_tasks(self):
        return self.session.query(TaskModel).all()
    
    
    def update_task(self, data, id):
        
        try:
            task = self.session.query(TaskModel).filter(TaskModel.id == id).first()
            
            task.title = data.title
            task.description = data.description
            
            self.session.commit()
        except Exception as ex:
            messagebox.showerror("Edit Task", "The task could not be edited")
        
        return
    
    
    def delete_task(self, id):
        try:
            task = self.session.query(TaskModel).filter(TaskModel.id == id).delete()
            self.session.commit()
        except Exception as ex:
             messagebox.showerror("Delete Task", "Could not delete task")
        
        return
    
    
    def change_status_task(self, status, id ):
        try:
            task = self.session.query(TaskModel).filter(TaskModel.id == id).first()
            task.status = status
            self.session.commit()
        except Exception as ex:
            messagebox.showerror("Change Status", "The task could not be change status")
        
        return 