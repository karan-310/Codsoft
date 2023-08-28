
import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        pass


root = tk.Tk()
root.title("To-Do List")

tasks_listbox = tk.Listbox(root, width=50)
tasks_listbox.pack(pady=10)


entry = tk.Entry(root, width=40)
entry.pack(pady=5)


add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.RIGHT, padx=5)


root.mainloop()
