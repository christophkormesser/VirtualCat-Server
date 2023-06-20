import socket

from client_tools import send_command
from utils.wrap_stats import wrap_stats
from models import OledInputModel

def get_pet(s: socket.socket, stats: OledInputModel):
    try:
     data = s.recv(1024)
     return data
    except socket.timeout:
       print("User did not pet!")
       return None