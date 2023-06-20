import asyncio
import socket
import selectors
from utils.accept_wrapper import accept_wrapper
from utils.service_connection import service_connection
from utils.get_ip import get_ip

async def start_server() :
    sel = selectors.DefaultSelector()

    #HOST = get_ip()
    HOST = "127.0.0.1"
    PORT = 8500

    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((HOST, PORT))
    lsock.listen()
    print(f"Listening on {(HOST, PORT)}")
    lsock.setblocking(False)
    sel.register(lsock, selectors.EVENT_READ, data=None)


    try:
        while True:
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    accept_wrapper(key.fileobj, sel)
                else:
                    service_connection(key, mask, sel)
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")
    finally:
        sel.close()
