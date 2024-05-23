from config import engine, Base

from models import TaskModel

def main():
    Base.metadata.create_all(engine)
    

if __name__ == "__main__":
    main()