from pydantic import BaseModel

class OledInputModel(BaseModel):
    game_mode: int
    rounds: int
    wins: int
    losses: int