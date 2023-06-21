import socket
import select

from utils.client_tools import send_command
from utils.wrap_stats import wrap_stats
from models import OledInputModel

def get_pet(s: socket.socket):
    """Waits for pets from the Proximity Nucleo.
    Args:
        s (socket.socket): The sending socket object
    Returns:
        bytes | None: Received data as bytes, None if timeout"""

    try:
     print("Ready for petting!")
     data = s.recv(1024)
     print("!-User pet the cat!")
     print("TCP RECEIVED: " + str(data))
     return data
    except socket.timeout:
       print("!-User did not pet!")
       return None