import tkinter as tk

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
    new_window.geometry("400x400")
    new_window.config(bg='#333')

    title_label = tk.Label(new_window, text="Title:", bg='#333', fg='white')
    title_label.pack(pady=10)

    title_entry = tk.Entry(new_window, bg='#333', fg='white', insertbackground='white')
    title_entry.pack(pady=10)

    text_label = tk.Label(new_window, text="Note:", bg='#333', fg='white')
    text_label.pack(pady=10)

    text = tk.Text(new_window, height=10, width=30, bg='#333', fg='white', insertbackground='white')
    text.pack(pady=10)

    save_button = tk.Button(new_window, text="Save Note", command=save_note, bg='#AA4499', fg='white')
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
root.geometry("400x400")
root.config(bg='#333')

add_button = tk.Button(root, text="Add Note", command=add_note, bg='#AA4499', fg='white')
add_button.pack(pady=10)

listbox = tk.Listbox(root, bg='#333', fg='white')
listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Note", command=delete_note, bg='#AA4499', fg='white')
delete_button.pack(pady=10)

root.mainloop()

