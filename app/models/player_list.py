"""Project OC DAP 4 file with tournament related class."""

from tinydb import TinyDB

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

    def save_tinyDB(self):
        """(Put description here)."""
        db = TinyDB("db.json")
        players_table = db.table("players")
        players_table.truncate()

        serialized_players = self.get_serialized_players()
        players_table.insert_multiple(serialized_players)

    def get_serialized_players(self):
        """(Put description here)."""
        serialized_players = []
        for player in self.content.values():
            serialized_players.append(player.return_serialized_player())

        return serialized_players
