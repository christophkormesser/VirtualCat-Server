from pydantic import BaseModel

# model/format needed for the OLED Nucleo
class OledInputModel(BaseModel):
    game_mode: int
    rounds: int
    wins: int
    losses: int