import os




TASK_FILE =os.path.join(os.path.dirname(__file__),"..","task.txt")

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE) as file:
        return[line.strip() for line in file if line.strip()]

def _save_tasks(tasks: list[str]):
    os.makedirs(os.path.dirname(TASK_FILE),exist_ok=True)
    with open(TASK_FILE, "w") as file:
      file.write("\n".join(tasks))

def add_task(description: str) -> str:
    tasks = load_tasks()
    tasks.append(description)
    _save_tasks(tasks)
    return f"Added Task: {description}"

def list_tasks() -> str:
    tasks = load_tasks()
    if not tasks:
        return "Your to-do list is empty"
    return "Your task: \n" + "\n".join(f"{i+1}. {t}" for i,t in enumerate(tasks))
       
def remove_task(index:int) -> str:
    tasks = load_tasks()
    if index<1 or index>len(tasks):
        return f"No task at position {index}"
    removed = tasks.pop(index-1)
    _save_tasks(tasks)
    return f"Removed tasks: {removed}"
    
   