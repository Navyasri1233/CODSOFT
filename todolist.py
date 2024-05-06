import tkinter as tk
from tkinter import messagebox
from tkinter import *


root=tk.Tk()
root.title("TO-DO LIST")
root.geometry("650x410+300+150")
root.resizable(0,0)
root.configure(bg="#FAEBD7")

label1=tk.Label(root,text="TO-DO-LIST",font="georgia 25 bold",width=10,bd=5,bg="#FAEBD7",fg="#8B4513")
label1.pack(side="top",fill=BOTH)

label2=tk.Label(root,text="ADD TASK",font="ariel 15 bold",width=10,bd=5,bg="#8B4513",fg="black")
label2.place(x=20,y=54)

label3=tk.Label(root,text=" TASKS",font="ariel 15 bold",width=10,bd=5,bg="#8B4513",fg="black")
label3.place(x=320,y=54)

task=[]

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

listbox_tasks = tk.Listbox(root,width=30, height=9,bd=2,font="ariel 20 italic bold")
listbox_tasks.place(x=200,y=100)

entry_task = tk.Entry(root, width=20,bd=2,font="ariel 10 italic bold")
entry_task.place(x=20,y=120)

button_add_task = tk.Button(root, text="ADD", width=10,font="sarif 15 bold",bg="#8B4513",fg="black" ,command=add_task)
button_add_task.place(x=20,y=200)

button_delete_task = tk.Button(root, text="DELETE", width=10, command=delete_task,font="sarif 15 bold",bg="#8B4513",fg="black")
button_delete_task.place(x=20,y=300)

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=listbox_tasks.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# scrollbar_tasks = tk.Scrollbar(listbox_tasks)
# scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

# Run the application
root.mainloop()