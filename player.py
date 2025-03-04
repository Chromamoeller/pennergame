import json
import os


class Player:
    def __init__(self, name="Penner"):
        self.name = name
        self.currency = 5  # Startgeld
        self.strength = 10
        self.energy = 10
        self.hunger = 5  # 0 = verhungert, 10 = satt
        self.weapon = None
        self.deposit_bottle = 0
        self.status = "Obdachlos"

        # Lade gespeicherte Daten (falls vorhanden)
        self.load_player()

    def work(self):
        """Verdiene Geld, verliere Energie"""
        if self.energy > 0:
            self.currency += 10
            self.energy -= 2
            print(f"{self.name} hat gearbeitet! +10€ Geld, -2 Energie")
        else:
            print("Zu erschöpft zum Arbeiten!")
        self.save_player()

    def eat(self):
        """Iss Essen, verliere Geld, erhalte Energie"""
        if self.currency >= 5:
            self.currency -= 5
            self.energy += 5
            self.hunger = min(self.hunger + 3, 10)
            print(f"{self.name} hat gegessen! -5€ Geld, +5 Energie")
        else:
            print("Nicht genug Geld für Essen!")
        self.save_player()

    def train(self):
        """Trainiere, um stärker zu werden, verliere Energie"""
        if self.energy >= 3:
            self.strength += 2
            self.energy -= 3
            print(f"{self.name} hat trainiert! +2 Stärke, -3 Energie")
        else:
            print("Zu müde zum Trainieren!")
        self.save_player()

    def collect_bottles(self):
        """Sammle Pfandflaschen, um Geld zu verdienen"""
        self.deposit_bottle += 5
        self.currency += 2
        print(f"{self.name} hat 5 Pfandflaschen gesammelt! +2€ Geld")
        self.save_player()

    def buy_weapon(self, weapon_name, price):
        """Kaufe eine Waffe, falls genug Geld da ist"""
        if self.currency >= price:
            self.currency -= price
            self.weapon = weapon_name
            print(f"{self.name} hat {weapon_name} gekauft! -{price}€ Geld")
        else:
            print("Nicht genug Geld für eine Waffe!")
        self.save_player()

    def rest(self):
        """Schlafen, um Energie zu regenerieren"""
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} hat geschlafen! +5 Energie")
        self.save_player()

    def show_status(self):
        """Zeigt den aktuellen Status des Spielers"""
        print(f"""
        --- {self.name}'s Status ---
        Geld: {self.currency} €
        Stärke: {self.strength}
        Energie: {self.energy}/10
        Hunger: {self.hunger}/10
        Waffe: {self.weapon if self.weapon else 'Keine'}
        Pfandflaschen: {self.deposit_bottle}
        Status: {self.status}
        ---------------------------
        """)

    def save_player(self):
        """Speichert den aktuellen Spielerstatus in einer JSON-Datei"""
        data = {
            "name": self.name,
            "currency": self.currency,
            "strength": self.strength,
            "energy": self.energy,
            "hunger": self.hunger,
            "weapon": self.weapon,
            "deposit_bottle": self.deposit_bottle,
            "status": self.status
        }

        # Speichert den Spieler unter "saves/{name}.json"
        os.makedirs("saves", exist_ok=True)  # Erstellt Ordner, falls nicht vorhanden
        with open(f"saves/{self.name}.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"✅ Spielstand gespeichert: saves/{self.name}.json")

    def load_player(self):
        """Lädt den Spielerstatus aus einer JSON-Datei"""
        file_path = f"saves/{self.name}.json"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
                self.currency = data["currency"]
                self.strength = data["strength"]
                self.energy = data["energy"]
                self.hunger = data["hunger"]
                self.weapon = data["weapon"]
                self.deposit_bottle = data["deposit_bottle"]
                self.status = data["status"]
            print(f"🔄 Spielstand für {self.name} geladen!")
        else:
            print("❌ Kein gespeicherter Spielstand gefunden. Neuer Spieler wird erstellt.")

