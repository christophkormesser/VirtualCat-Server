import socket
from datetime import datetime

def establish_connection(host: str, port: int):
    """Establishes connection to a TCP Socket.
    
    Args:
        host (str): IP Address of the TCP Server
        port (int): Port the TCP Server listens on
    Returns:
        socket.socket: The established socket object
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    return s


def send_command(s: socket.socket, command: str):
    """Sends a command to a socket.
    
    Args:
        s (socket.socket): The receiving socket object
        command (str): The command to be sent
    """
    
    s.sendall(bytes(command, "utf-8"))
    
    # logging
    data_sent = bytes(str((datetime.now().hour)) + ":" + 
                 str(datetime.now().minute)+ ":" + 
                 str(datetime.now().second) + "  " +
                 command, "utf-8")
    print(data_sent.decode("utf-8"))
