# Virtual Cat – Proxy & Game Logic

## What's happening?

First, the OLED Nucleo starts an Access Point and a TCP Server.
Then the Proximity Nucleo connects to the Access Point and starts a TCP Server as well.

After both Nucleos are up and running the Laptop starts the python code from `main.py`:

1. A connection to the Wifi Access Point (OLED Nucleo) is established as well as to its TCP Server.
2. The connection to the Proximity Nucleo TCP Server is established.
3. The stats (mood/state, rounds, wins, losses) are initialized.
4. The Startup action is triggered at the OLED Nucleo.
5. Now the game loop is entered.
6. A mood is calculated and sent to the OLED Nucleo.
7. The code listens for user action at the Proximity Nucleo.
8. The cats reaction is bein calculated and sent to the OLED Nucleo.
9. Loop till 5 rounds are reached. (Jump to step 6)
10. Game Over after 5 rounds

## Project Members

| Name                  | Username |
|-----------------------|----------|
| Johanna Gaudeck       | ic21b048 |
| Aelfric Wieland Mayer | ic21b111 |
| Christoph Kormesser   | ic21b004 |
