from windowHandler import *
from utility import *
from player import Player

player_main = Player("")

root = tk.Tk()
# Setup
window_x_size = 900
window_y_size = 600
root.geometry(f"{window_x_size}x{window_y_size}")
root.resizable(False, False)
root.title("Penner Game")

# Header
top_frame = tk.Frame(root, bg="gray", height=50)
top_frame.pack(fill="x")

title_lable = tk.Label(top_frame, text="Pennergame", font=("Arial", 14))
title_lable.pack(pady=10)

# MainFrame
playerstats_frame = tk.Frame(root, height=50, bg="gray")
playerstats_frame.pack(fill="x")
main_frame = tk.Frame(root, bg="white")
main_frame.pack(expand=True, fill="both")

player_bottle_count = tk.Label(main_frame, text="")

player_name_label = tk.Label(playerstats_frame, text="😀Name:", font="arial")
player_name_label.place(x=window_x_size - 890, y=10)
player_name_value_label = tk.Label(playerstats_frame, text=f"Christian", font="arial")
player_name_value_label.place(x=window_x_size - 810, y=10)

player_hunger_label = tk.Label(playerstats_frame, text="🍴 Hunger:", font="arial")
player_hunger_label.place(x=window_x_size - 735, y=10)
player_hunger_value_label = tk.Label(playerstats_frame, text=f"{player_main.currency}", font="arial")
player_hunger_value_label.place(x=window_x_size - 645, y=10)

player_weapon_label = tk.Label(playerstats_frame, text="🗡Waffe:", font="arial")
player_weapon_label.place(x=window_x_size - 620, y=10)
player_weapon_value_label = tk.Label(playerstats_frame, text=f"Fäuste", font="arial")
player_weapon_value_label.place(x=window_x_size - 543, y=10)

player_energy_label = tk.Label(playerstats_frame, text="⚡Energie:", font="arial")
player_energy_label.place(x=window_x_size - 410, y=10)
player_energy_value_label = tk.Label(playerstats_frame, text=f"{player_main.currency}", font="arial")
player_energy_value_label.place(x=window_x_size - 330, y=10)

player_strength_label = tk.Label(playerstats_frame, text="💪 Stärke:", font="arial")
player_strength_label.place(x=window_x_size - 310, y=10)
player_strength_value_label = tk.Label(playerstats_frame, text=f"{player_main.currency}", font="arial")
player_strength_value_label.place(x=window_x_size - 230, y=10)

player_bottle_label = tk.Label(playerstats_frame, text="🍾 Flaschen:", font="arial")
player_bottle_label.place(x=window_x_size - 210, y=10)
player_bottle_value_label = tk.Label(playerstats_frame, text=f"{player_main.currency}", font="arial")
player_bottle_value_label.place(x=window_x_size - 110, y=10)

player_curency_label = tk.Label(playerstats_frame, text="💰 Geld:", font="arial")
player_curency_label.place(x=window_x_size - 90, y=10)
player_curency_value_label = tk.Label(playerstats_frame, text=f"{player_main.currency}", font="arial")
player_curency_value_label.place(x=window_x_size - 20, y=10)

# Footer
bottom_frame = tk.Frame(root, bg="gray", height=50)
bottom_frame.pack(fill="x")

working_btn = tk.Button(bottom_frame, text="Arbeiten",
                        command=lambda: get_money(player_main, player_curency_value_label))
working_btn.pack(pady=10)
open_popup(root, player_main, top_frame, player_curency_value_label, player_bottle_value_label, player_name_value_label,
           player_hunger_value_label, player_weapon_value_label, player_energy_value_label, player_strength_value_label)

root.mainloop()
