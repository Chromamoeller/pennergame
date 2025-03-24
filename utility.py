
def get_money(player, player_curency_value_label):
    player.currency +=10
    player_curency_value_label.config(text=f"{player.currency} €")
