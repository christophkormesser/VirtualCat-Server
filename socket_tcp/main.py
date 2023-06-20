from client_tools import establish_connection
from states.startup import startup
from states.moodsetter import set_mood
from utils.get_pet import get_pet
from states.show_happy import show_happy
from states.show_angry import show_angry
from states.show_gameover import show_gameover
from models import OledInputModel

from time import sleep
import random


def main():

    # connects to oled nucleo and returns socket
    print("Establishing connection to OLED Nucleo...")
    socket_oled = establish_connection("192.168.0.1", 8500)
    socket_oled.settimeout(20.0)
    print("Connection established: ", socket_oled)

    # connects to proximity nucleo and returns socket
    print("Establishing connection to Proximity Nucleo...")
    #socket_proximity = establish_connection("192.168.0.5", 8500)
    #socket_proximity.settimeout(5.0)
    #print("Connection established: ", socket_proximity)

    stats = OledInputModel(game_mode=1,rounds=0,wins=0,losses=0)
       

    # starts welcome screen
    startup(socket_oled, stats)
    sleep(3)

    # game loop
    while True:
        stats.rounds += 1

        mood = set_mood(socket_oled, stats)

        # listen for user action
        #action = get_pet(socket_proximity, stats)
        sleep(14)

        action = random.randint(0,1)
        if(action == 0):
            action = None
            print("User did not pet the cat.")
        else:
            print("User petted the cat!")

        if action is not None:
            # pet
            if mood == 2:
                # sad
                stats.wins += 1
                show_happy(socket_oled, stats)
            if mood == 3:
                # angry
                stats.losses += 1
                show_angry(socket_oled, stats)
        else:
            # no pet
            if mood == 2:
                # sad
                stats.losses += 1
                show_angry(socket_oled, stats)
            if mood == 3:
                stats.wins += 1
                show_happy(socket_oled, stats)

        # wait for animation
        sleep(12)
            
        if(stats.rounds < 5):
            continue
        else:
            show_gameover(socket_oled, stats)
            stats.game_mode = 1
            stats.rounds = 0
            stats.wins = 0
            stats.losses = 0
            sleep(5)
        

            

    

    # game loop

main()