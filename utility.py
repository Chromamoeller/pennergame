
def get_money(player, player_curency_value_label):
    player["currency"] +=10
    player_curency_value_label.config(text=f"{player['currency']} €")

def collect_deposit_bottle(player):
    player["deposit_bottle"] += 5
