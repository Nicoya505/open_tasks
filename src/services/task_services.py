
from models import TaskModel

class TaskServices:
    def __init__(self, session):
        self.session = session
    
    
    def create_task(self, task):
        
        self.session.add(task)
        self.session.commit()
        
        return
    
    
    def get_tasks(self):
        return self.session.query(TaskModel).all()
    
    
    def update_task(self, data, id):
        task = self.session.query(TaskModel).filter(TaskModel.id == id).first()
        
        task.title = data.title
        task.description = data.description
        
        self.session.commit()
        
        return
    
    
    def delete_task(self, id):
        task = self.session.query(TaskModel).filter(TaskModel.id == id).delete()
        self.session.commit()
        
        return 