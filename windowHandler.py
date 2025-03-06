import tkinter as tk
import json
import os

json_datei = "users.json"


# Funktion zum Laden der Benutzerdaten aus einer JSON-Datei
def load_users():
    if not os.path.exists("users.json"):  # Falls die Datei nicht existiert
        return {}  # Gebe ein leeres Dictionary zurück

    try:
        with open("users.json", "r") as file:
            data = file.read().strip()  # Strip entfernt Leerzeichen oder neue Zeilen
            if not data:  # Falls die Datei leer ist
                return {}
            return json.loads(data)  # JSON-Daten parsen
    except (json.JSONDecodeError, ValueError):  # Fehler beim Parsen der JSON-Datei
        print("❌ Fehler: users.json ist beschädigt. Datei wird neu erstellt.")
        return {}


def save_json(data):
    with open(json_datei, "w") as file:
        json.dump(data, file, indent=4)
    print("erfolgreich gespeichert")


# Funktion zum Laden eines gespeicherten Spielers
def load_player(name):
    file_path = f"saves/{name}.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return None  # Falls kein Speicherstand existiert


# Funktion zum Speichern eines neuen Spielers
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


# **Neue Funktion zum Aktualisieren der UI nach dem Laden des Spielers**
def update_ui(player, player_curency_value_label, player_deposit_bottle, player_name_value_label,
              player_hunger_value_label, player_weapon_value_label, player_energy_value_label,
              player_strength_value_label):
    player_curency_value_label.config(text=f"{player.currency} €")
    player_deposit_bottle.config(text=f"{player.deposit_bottle}")
    player_name_value_label.config(text=f"{player.name}")
    player_hunger_value_label.config(text=f"{player.hunger}")
    player_weapon_value_label.config(text=f"{player.weapon}")
    player_energy_value_label.config(text=f"{player.energy}")
    player_strength_value_label.config(text=f"{player.strength}")


# Funktion zum Öffnen des Login-Fensters
def open_popup(root, player, player_curency_value_label, player_bottle_value_label, player_name_value_label,
               player_hunger_value_label, player_weapon_value_label, player_energy_value_label,
               player_strength_value_label):
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

                # **Ruft update_ui() auf, um die Anzeige zu aktualisieren**
                update_ui(player, player_curency_value_label, player_bottle_value_label, player_name_value_label,
                          player_hunger_value_label, player_weapon_value_label, player_energy_value_label,
                          player_strength_value_label)

            else:
                error_label.config(text="❌ Kein Spielstand gefunden!")
        else:
            error_label.config(text="❌ Falscher Benutzername oder Passwort!")

    # Buttons für Login und Registrierung
    btn_frame = tk.Frame(popup)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="OK", command=submit).pack(side="left", padx=10)
    tk.Button(btn_frame, text="Account erstellen", command=open_window_new_account).pack(side="left", padx=10)


def open_window_new_account():
    popup = tk.Toplevel()
    popup.title("Neuer Account")
    popup.attributes("-topmost", True)
    popup_width = 300
    popup_height = 250
    popup.geometry(f"{popup_width}x{popup_height}")

    tk.Label(popup, text="Name").pack()
    new_acc_name = tk.Entry(popup, font="Arial")
    new_acc_name.pack(pady=10)
    tk.Label(popup, text="Passwort").pack()
    new_account_password = tk.Entry(popup, show="*", font="Arial")
    new_account_password.pack(pady=10)

    def add_user_to_list():
        username = new_acc_name.get().strip()
        password = new_account_password.get().strip()

        if not username or not password:
            print("❌ Benutzername und Passwort dürfen nicht leer sein!")
            return

        user_list = load_users()

        if username in user_list:
            print("❌ Benutzername existiert bereits!")
        else:
            user_list[username] = password
            save_json(user_list)  # ✅ Korrektur: user_list speichern, nicht "list"
            user_data_name = f"{new_acc_name.get()}"
            user_data = {
                "name": f"{new_acc_name.get()}",
                "currency": 5,
                "strength": 20,
                "energy": 10,
                "hunger": 10,
                "weapon": "Schlagring",
                "deposit_bottle": 0,
                "status": "Obdachlos"
            }

            verzeichnis = f"./saves/{user_data_name}.json"
            with open(verzeichnis, "w") as file:
                json.dump(user_data, file, indent=4)
            print("✅ Neuer Benutzer erfolgreich registriert!")

    tk.Button(popup, text="Regestrieren", command=add_user_to_list).pack()
