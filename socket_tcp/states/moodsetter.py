import random, socket
from models import OledInputModel
from utils.client_tools import send_command
from utils.wrap_stats import wrap_stats

def set_mood(socket: socket.socket, stats: OledInputModel):
    """Calculates randomly the mood (sad/angry) and sends it to the OLED Nucleo.
    Args:
        socket (socket.socket): receiving socket object
        stats (OledInputModel): Stats of the game - stats.game_mode handles display animation at Nucleo
    Returns:
        int: The calculated mood"""
    
    global current_mood
    current_mood= random.randint(2, 3)

    if(current_mood == 2):
        print("Cat is sad right now :'(")
    elif(current_mood == 3):
        print("Cat is angry! >:(")

    stats.game_mode = current_mood
    stat_string = wrap_stats(stats)

    send_command(socket, stat_string)
    
    return current_mood
