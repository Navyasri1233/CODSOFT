
import tkinter as tk
from tkinter import messagebox
from tkinter import *

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    if name != "" and phone != "":
        contact_list.insert(tk.END, f"{name}: {phone}")
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter both name and phone number.")

def delete_contact():
    try:
        selected_contact = contact_list.curselection()[0]
        contact_list.delete(selected_contact)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a contact to delete.")

# Create main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("650x410+300+150")
root.resizable(0,0)
root.configure(bg="lightblue")


# Create UI elements
# frame_contacts = tk.Frame(root)
# frame_contacts.pack()
#listbox_tasks = tk.Listbox(root,width=30, height=9,bd=2,font="ariel 20 italic bold")
#listbox_tasks.place(x=200,y=100)

contact_list = tk.Listbox(root, width=22, height=10,bd=2,font="ariel 20 italic bold")
contact_list.place(x=300,y=50)

scrollbar_contacts = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar_contacts.pack(side=tk.RIGHT, fill=tk.Y)

contact_list.config(yscrollcommand=scrollbar_contacts.set)
scrollbar_contacts.config(command=contact_list.yview)
'''
frame_entry = tk.Frame(root)
frame_entry.pack()
'''
label1=tk.Label(root,text="CONTACT BOOK",font="georgia 25 bold",width=10,bd=5,bg="lightblue",fg="#8B4513")
label1.pack(side="top",fill=BOTH)

label_name = tk.Label(root, text="Name:",bg="lightblue",font='arial 15 bold')
label_name.place(x=20,y=50)

entry_name = tk.Entry(root, width=30)
entry_name.place(x=20,y=80)

label_phone = tk.Label(root, text="Phone:",bg="lightblue",font='arial 15 bold')
label_phone.place(x=20,y=110)

entry_phone = tk.Entry(root, width=30)
entry_phone.place(x=20,y=140)

button_add_task = tk.Button(root, text="Add contact", width=15,font="sarif 15 bold",bg="#B0E0E6",fg="black" ,command=add_contact)
button_add_task.place(x=20,y=200)

button_delete_task = tk.Button(root, text="Delete contact", width=15, command=delete_contact,font="sarif 15 bold",bg="#B0E0E6",fg="black")
button_delete_task.place(x=20,y=300)

# Run the application
root.mainloop()