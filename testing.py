import tkinter as tk

def open_popup():
    popup = tk.Toplevel(root)
    popup.title("Zentriertes Popup")
    popup.attributes("-topmost", True)  # Immer im Vordergrund

    # Größe des Popups
    popup_width = 300
    popup_height = 150

    # Warte, bis das Hauptfenster die korrekte Größe hat
    root.update_idletasks()

    # Größe und Position des Hauptfensters abrufen
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()

    # Position für zentriertes Popup berechnen
    x = root_x + (root_width - popup_width) // 2
    y = root_y + (root_height - popup_height) // 2

    # Fenster an der berechneten Position öffnen
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    tk.Label(popup, text="Ich bin genau zentriert!").pack(pady=10)
    tk.Button(popup, text="Schließen", command=popup.destroy).pack(pady=5)

root = tk.Tk()
root.geometry("600x400")  # Hauptfenstergröße

btn = tk.Button(root, text="Popup öffnen", command=open_popup)
btn.pack(pady=20)

root.mainloop()

