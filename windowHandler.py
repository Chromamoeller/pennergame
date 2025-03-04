import tkinter as tk
import json
import os

# Funktion zum Laden der Benutzerdaten aus einer JSON-Datei
def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Falls Datei nicht existiert, leere Liste zurückgeben

# Funktion zum Speichern der Benutzerdaten in der JSON-Datei
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# Funktion zum Laden eines gespeicherten Spielers
def load_player(name):
    file_path = f"saves/{name}.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return None  # Falls kein Speicherstand existiert

# Funktion zum Speichern eines neuen Spielers
def save_player(player_data):
    os.makedirs("saves", exist_ok=True)  # Erstellt den Ordner "saves", falls nicht vorhanden
    file_path = f"saves/{player_data['name']}.json"
    with open(file_path, "w") as file:
        json.dump(player_data, file, indent=4)

# Funktion zum Öffnen des Registrierungsfensters
def open_registration():
    reg_popup = tk.Toplevel()
    reg_popup.title("Registrierung")
    reg_popup.geometry("300x250")
    reg_popup.attributes("-topmost", True)

    tk.Label(reg_popup, text="Neuer Username:").pack(pady=5)
    new_username_entry = tk.Entry(reg_popup, font="Arial")
    new_username_entry.pack(pady=5)

    tk.Label(reg_popup, text="Neues Passwort:").pack(pady=5)
    new_password_entry = tk.Entry(reg_popup, show="*", font="Arial")
    new_password_entry.pack(pady=5)

    reg_error_label = tk.Label(reg_popup, text="", fg="red")
    reg_error_label.pack(pady=5)

    def register():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()

        if not new_username or not new_password:
            reg_error_label.config(text="❌ Alle Felder ausfüllen!")
            return

        users = load_users()

        if new_username in users:
            reg_error_label.config(text="❌ Benutzername existiert bereits!")
        else:
            users[new_username] = new_password
            save_users(users)

            # Standard-Spielstand für neuen Spieler speichern
            new_player_data = {
                "name": new_username,
                "currency": 5,
                "strength": 10,
                "energy": 10,
                "hunger": 5,
                "weapon": None,
                "deposit_bottle": 0,
                "status": "Obdachlos"
            }
            save_player(new_player_data)

            reg_error_label.config(text="✅ Account erstellt!", fg="green")
            reg_popup.after(1000, reg_popup.destroy)  # Fenster nach 1 Sekunde schließen

    tk.Button(reg_popup, text="Speichern", command=register).pack(pady=10)

# Funktion zum Öffnen des Login-Fensters
def open_popup(root, player, top_frame):
    popup = tk.Toplevel(root)
    popup.title("Login")
    popup.attributes("-topmost", True)
    popup_width = 300
    popup_height = 250

    root.update_idletasks()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()

    x = root_x + (root_width - popup_width) // 2
    y = root_y + (root_height - popup_height) // 2
    popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

    tk.Label(popup, text="Username:").pack(pady=5)
    username_entry = tk.Entry(popup, font="Arial")
    username_entry.pack(pady=5)

    tk.Label(popup, text="Password:").pack(pady=5)
    password_entry = tk.Entry(popup, show="*", font="Arial")
    password_entry.pack(pady=5)

    error_label = tk.Label(popup, text="", fg="red")
    error_label.pack(pady=5)

    def submit():
        username = username_entry.get()
        password = password_entry.get()
        users = load_users()

        # Prüfen, ob Benutzername und Passwort korrekt sind
        if username in users and users[username] == password:
            saved_data = load_player(username)
            if saved_data:
                # Spieler-Objekt mit gespeicherten Daten aktualisieren
                player.name = saved_data["name"]
                player.currency = saved_data["currency"]
                player.strength = saved_data["strength"]
                player.energy = saved_data["energy"]
                player.hunger = saved_data["hunger"]
                player.weapon = saved_data["weapon"]
                player.deposit_bottle = saved_data["deposit_bottle"]
                player.status = saved_data["status"]

                popup.destroy()  # Fenster schließen
                player_name_label = tk.Label(top_frame, text=f"Eingeloggt als: {player.name}", font=("Arial", 14))
                player_name_label.pack(pady=20)
            else:
                error_label.config(text="❌ Kein Spielstand gefunden!")
        else:
            error_label.config(text="❌ Falscher Benutzername oder Passwort!")

    # Buttons für Login und Registrierung
    btn_frame = tk.Frame(popup)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="OK", command=submit).pack(side="left", padx=10)
    tk.Button(btn_frame, text="Neuen Account erstellen", command=open_registration).pack(side="right", padx=10)
