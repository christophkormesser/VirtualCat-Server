import socket
from models import OledInputModel
from utils.client_tools import send_command
from utils.wrap_stats import wrap_stats

def show_gameover(s: socket.socket, stats: OledInputModel):
    stats.game_mode = 6
    stat_string = wrap_stats(stats)

    send_command(s, stat_string)