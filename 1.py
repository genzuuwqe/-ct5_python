import tkinter as tk
from datetime import datetime, date

def load_tasks(filename="tasks.txt"):
    loaded_tasks = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("|")
            if len(parts) == 3:
                event = parts[0].strip()
                date_str = parts[1].strip()
                type = parts[2].strip()
                loaded_tasks.append((event,date_str,type))
    return loaded_tasks

TASKS = load_tasks()

def diff(target_date):
    target_date = datetime.strptime(target_date, "%d.%m.%Y").date()
    today = date.today()
    delta = target_date - today
    return delta.days

def tasks(parent,event,date_str,type):
    days = diff(date_str)

    if type == "past" or days < 0:
        text = f"Прошло {abs(days)} дней от {event}"
        color = "red"
        
    elif type == "today" or days == 0:
        text = f"Прямо щас: {event}"
        color = "yellow"
    else:
        text = f"Осталось {days} дней до {event}"
        color = "gray"

    label = tk.Label(
        parent, 
        text=text,
        font=("Arial",12),
        fg=color,
        bg= "black",
        anchor="w"
    )
    return label

root = tk.Tk()
root.title("Что мне делать, как мне жить?")
root.geometry("700x400")
root.configure(bg="black")

header = tk.Label(root, text= "Мои текущие задачи", font=("Arial",24,"underline", "bold"),fg= "yellow", bg="black")
header.pack(pady=30)

tasks_frame = tk.Frame(root, bg="black")
tasks_frame.pack(fill=tk.BOTH, expand=True, padx=200)

sorted_tasks = sorted(TASKS, key=lambda x: diff(x[1]))

for event, date_str, type in sorted_tasks:
    lbl = tasks(tasks_frame,event,date_str,type)
    lbl.pack(anchor="w", pady=5)

root.mainloop()
