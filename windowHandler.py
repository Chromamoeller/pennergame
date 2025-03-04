import tkinter as tk

def open_popup(root, player, top_frame):
    # Neues Fenster erstellen
    popup = tk.Toplevel(root)
    popup.title("Name des Spielers")
    #popup.geometry("300x150")
    popup.attributes("-topmost", True)
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

    # Label für die Eingabe
    tk.Label(popup, text="Wie lautet dein name?:").pack(pady=5)

    # Entry-Feld
    entry = tk.Entry(popup)
    entry.pack(pady=5)
    # Bestätigungsbutton
    def submit():
        player["name"] = entry.get()
        popup.destroy()  # Schließt das Fenster nach der Eingabe
        player_name_lable = tk.Label(top_frame, text=f"Eingeloggt als: {player["name"]} ", font=("Arial", 14))
        player_name_lable.pack(pady=20)
    tk.Button(popup, text="OK", command=submit).pack(pady=10)