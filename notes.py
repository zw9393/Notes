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

    title_label = tk.Label(new_window, text="Title:")
    title_label.pack(pady=10)

    title_entry = tk.Entry(new_window)
    title_entry.pack(pady=10)

    text_label = tk.Label(new_window, text="Note:")
    text_label.pack(pady=10)

    text = tk.Text(new_window, height=10, width=30)
    text.pack(pady=10)

    save_button = tk.Button(new_window, text="Save Note", command=save_note)
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

add_button = tk.Button(root, text="Add Note", command=add_note)
add_button.pack(pady=10)

listbox = tk.Listbox(root)
listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Note", command=delete_note)
delete_button.pack(pady=10)

root.mainloop()

