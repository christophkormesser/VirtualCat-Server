import socket
from datetime import datetime

def establish_connection(host: str, port: int):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    return s


def send_command(s: socket.socket, command: str):
    
    s.sendall(bytes(command, "utf-8")) # sends command to Nucleo
    #data = s.recv(1024) # waits for ACK
    
    data_sent = bytes(str((datetime.now().hour)) + ":" + 
                 str(datetime.now().minute)+ ":" + 
                 str(datetime.now().second) + "  " +
                 command, "utf-8")
    print(data_sent.decode("utf-8"))

    #return data
