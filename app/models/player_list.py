"""Project OC DAP 4 file with tournament related class."""

from app.models.player import Player


class PlayerList:
    """Player characteristics to be handled by application."""

    def __init__(self):
        """Init Player class."""
        self.content = {}

    def add_player(self, name, surname, birth, gender, ranking):
        """(Put description here)."""
        player_index = name + surname
        self.content[player_index] = Player(name, surname, birth, gender, ranking)

        return player_index
