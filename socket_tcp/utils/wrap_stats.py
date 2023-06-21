from models import OledInputModel

def wrap_stats(obj: OledInputModel) -> str:
    """Converts the stats object into a readable string for the OLED Nucleo
    Args:
        obj (OledInputModel): Stats to be converted
    Returns:
        str: The converted string"""
    
    string = str(obj.game_mode) + "," + \
            str(obj.rounds) + "," + \
            str(obj.wins) + "," + \
            str(obj.losses)
    
    return string