import socket
from models import OledInputModel
from client_tools import send_command
from utils.wrap_stats import wrap_stats

def show_angry(s: socket.socket, stats: OledInputModel):
    stats.game_mode = 4
    stat_string = wrap_stats(stats)

    send_command(s, stat_string)