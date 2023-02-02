import tkinter as tk
from tkinter import font

notes = []

def add_note():
    def save_note():
        title = title_entry.get()
        if not title:
            return
        note = text.get("1.0", tk.END)
        notes.append((title, note))
        new_window.destroy()
        update_list()

    new_window = tk.Toplevel(root)
    new_window.title("Add Note")
    new_window.geometry("800x800")
    new_window.configure(bg="#ffffff")

    title_label = tk.Label(new_window, text="Title:", font=("Open Sans", 14), bg="#ffffff", fg="#555555")
    title_label.pack(pady=10)

    title_entry = tk.Entry(new_window, font=("Open Sans", 14), bd=2, relief="groove")
    title_entry.pack(pady=10)

    text_label = tk.Label(new_window, text="Note:", font=("Open Sans", 14), bg="#ffffff", fg="#555555")
    text_label.pack(pady=10)

    text = tk.Text(new_window, height=10, width=30, font=("Open Sans", 14), bd=2, relief="groove")
    text.pack(pady=10)

    save_button = tk.Button(new_window, text="Save Note", command=save_note, font=("Open Sans", 14), bg="#4A90E2", fg="#ffffff", relief=tk.FLAT, bd=0, borderwidth=0, highlightthickness=0, activebackground='#4A90E2', activeforeground='#ffffff')
    save_button.pack(pady=10)



def delete_note():
    index = listbox.curselection()
    if not index:
        return
    index = int(index[0])
    del notes[index]
    update_list()

def update_list():
    listbox.delete(0, tk.END)
    for i, (title, note) in enumerate(notes):
        listbox.insert(i, title)

root = tk.Tk()
root.title("Note Taking Application")
root.geometry("800x500")
root.configure(bg="#ffffff")

add_button = tk.Button(root, text="Add Note", command=add_note, font=("Open Sans", 14), bg="#4A90E2", fg="#ffffff", relief=tk.FLAT, bd=0)
add_button.pack(pady=10)

listbox = tk.Listbox(root, bg='#ffffff', fg='#555555', height=20, width=50, font=("Open Sans", 12))
listbox.pack(pady=10, padx=10)

delete_button = tk.Button(root, text="Delete Note", command=delete_note, font=("Ubuntu", 14), bg="purple", fg="white", relief=tk.FLAT, bd=0)
delete_button.pack(pady=10)

root.mainloop()

