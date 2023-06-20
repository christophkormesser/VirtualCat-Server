from models import OledInputModel

def wrap_stats(obj: OledInputModel) -> str:
    string = str(obj.game_mode) + "," + \
            str(obj.rounds) + "," + \
            str(obj.wins) + "," + \
            str(obj.losses)
    
    return string