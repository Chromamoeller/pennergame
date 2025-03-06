from windowHandler import *
from utility import *
from player import Player
player_main = Player("")


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
player_curency_value_label = tk.Label(main_frame, text=f"{player_main.currency}", font="arial")
player_curency_value_label.place(x=window_x_size-50, y=10)


#Footer
bottom_frame = tk.Frame(root, bg="gray", height=50)
bottom_frame.pack(fill="x")

btn = tk.Button(bottom_frame, text="Arbeiten", command=lambda: get_money(player_main,player_curency_value_label))
btn.pack(pady=10)
open_popup(root, player_main, top_frame, player_curency_value_label)

root.mainloop()
