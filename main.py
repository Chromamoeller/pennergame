import tkinter as tk
from utility import *

player = {
    "name":"",
    "currency": 500,
    "strength" : 10,
    "energy": 10,
    "pet": "",
    "weapon": "",
    "deposit_bottle": 0
}
def open_popup():
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

root = tk.Tk()
#Setup
window_x_size = 800
window_y_size = 600
root.geometry(f"{window_x_size}x{window_y_size}")
root.resizable(False, False)
root.title("Penner Game")

#Header
top_frame = tk.Frame(root, bg="gray", height=50)
top_frame.pack(fill="x")

title_lable = tk.Label(top_frame, text="Pennergame", font=("Arial", 14))
title_lable.pack(pady=10)



#MainFrame
main_frame = tk.Frame(root, bg="white")
main_frame.pack(expand=True, fill="both")

player_curency_label = tk.Label(main_frame, text="Geld:", font="arial").place(x=window_x_size-100, y=10)
player_curency_value_label = tk.Label(main_frame, text=f"{player['currency']}", font="arial")
player_curency_value_label.place(x=window_x_size-50, y=10)


#Footer
bottom_frame = tk.Frame(root, bg="gray", height=50)
bottom_frame.pack(fill="x")

btn = tk.Button(bottom_frame, text="Arbeiten", command=lambda: get_money(player,player_curency_value_label))
btn.pack(pady=10)
open_popup()

root.mainloop()
