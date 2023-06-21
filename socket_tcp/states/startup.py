from models import OledInputModel
from utils.client_tools  import send_command
from utils.wrap_stats import wrap_stats
import socket


def startup(s: socket.socket, stats: OledInputModel):
    """Sends startup gamemode to OLED Nucleo.
    Args:
        s (socket.socket): receiving socket object
        stats: (OledInputModel): Stats of the game - stats.game_mode handles display animation at Nucleo
    """

    stat_string = wrap_stats(stats)

    response = None

    while(response != "ACK\r\n"):
        send_command(s, stat_string)
        response = s.recv(1024) # waits for ACK
        response = response.decode("utf-8")
        print(f"Startup Response: {response}")
