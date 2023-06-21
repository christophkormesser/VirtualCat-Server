from models import OledInputModel
from utils.client_tools import establish_connection
from utils.get_pet import get_pet
from states.startup import startup
from states.moodsetter import set_mood
from states.show_happy import show_happy
from states.show_angry import show_angry
from states.show_gameover import show_gameover

from time import sleep


def main():
    """Handles the game setup, logic and loop."""

    # connects to oled nucleo and returns socket
    print("Establishing connection to OLED Nucleo...")
    socket_oled = establish_connection("192.168.0.1", 8500)
    socket_oled.settimeout(20.0)
    print("Connection established: ", socket_oled)

    # connects to proximity nucleo and returns socket
    print("Establishing connection to Proximity Nucleo...")
    socket_proximity = establish_connection("192.168.0.5", 8500)
    socket_proximity.settimeout(15.0)
    print("Connection established: ", socket_proximity)

    # initializes stats
    stats = OledInputModel(game_mode=1,rounds=0,wins=0,losses=0)
       

    # starts welcome screen
    startup(socket_oled, stats)
    sleep(3)

    # game loop
    while True:
        stats.rounds += 1

        # set mood to either sad or angry
        mood = set_mood(socket_oled, stats)

        # listen for user action
        action = get_pet(socket_proximity)
        
        sleep(8)

        # calculate the cats reaction using
        # the action in context of the cats mood
        if action is not None:
            # pet
            if mood == 2:
                # mood was sad, cat is now happy
                stats.wins += 1
                print("Cat is happy that you pet it!")
                show_happy(socket_oled, stats)
            if mood == 3:
                # mood was angry, cat is now super angry
                stats.losses += 1
                print("Cat is angry and scratches you!")
                show_angry(socket_oled, stats)
        else:
            # no pet happened
            if mood == 2:
                # mood was sad, cat gets angry
                stats.losses += 1
                print("Cat is angry and scratches you!")
                show_angry(socket_oled, stats)
            if mood == 3:
                # mood angry, cat is now happy
                stats.wins += 1
                print("Cat is happy that you left her alone!")
                show_happy(socket_oled, stats)

        # wait for animation
        sleep(12)
        
        # check if maximum number of 5 rounds has been played
        if(stats.rounds < 5):
            continue
        else:
            show_gameover(socket_oled, stats)
            stats.game_mode = 1
            stats.rounds = 0
            stats.wins = 0
            stats.losses = 0
            sleep(15)
            # start game from the start
            startup(socket_oled, stats)

        # remove input data from sensor
        print("Flushing TCP...")
        socket_proximity.settimeout(1)
        data = get_pet(socket_proximity)
        if data is not None:
            print("TCP CLEARED - " + str(data))
        socket_proximity.settimeout(15.0)
    

# execute main function
main()