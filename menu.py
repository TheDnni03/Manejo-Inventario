import tkinter as tk
import sqlite3

def insert_data(entry_name, entry_age):
    name = entry_name.get()
    age = entry_age.get()

    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # Insert data
    c.execute("INSERT INTO data (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

    # Close the connection
    conn.close()

def search_data(entry_id, text_display):
    id_to_search = entry_id.get()

    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # Retrieve data for the specified ID
    c.execute("SELECT * FROM data WHERE id=?", (id_to_search,))
    data = c.fetchone()

    # Clear the text display
    text_display.delete('1.0', tk.END)

    if data:
        text_display.insert(tk.END, f"ID: {data[0]}, Name: {data[1]}, Age: {data[2]}")
    else:
        text_display.insert(tk.END, "No se encontró ningún registro con ese ID.")

    # Close the connection
    conn.close()

def create_window():
    window = tk.Tk()
    window.title("Ingresar y Buscar Datos")
    window.geometry("600x500")

    label_name = tk.Label(window, text="Nombre:")
    label_name.pack()

    entry_name = tk.Entry(window)
    entry_name.pack()

    label_age = tk.Label(window, text="Edad:")
    label_age.pack()

    entry_age = tk.Entry(window)
    entry_age.pack()

    button_insert = tk.Button(window, text="Insertar Datos", command=lambda: insert_data(entry_name, entry_age))
    button_insert.pack()

    label_id = tk.Label(window, text="ID a buscar:")
    label_id.pack()

    entry_id = tk.Entry(window)
    entry_id.pack()

    text_display = tk.Text(window, height=5, width=40)
    text_display.pack()

    button_search = tk.Button(window, text="Buscar por ID", command=lambda: search_data(entry_id, text_display))
    button_search.pack()

    button_exit = tk.Button(window, text="Exit", command=window.quit)
    button_exit.pack()

    return window

def main():
    window = create_window()
    window.mainloop()

if __name__ == "__main__":
    main()
