"""Project OC DAP 4 file with tournament related class."""

from tinydb import TinyDB


class Player:
    """Player characteristics to be handled by application."""

    get_all: dict = {}

    def __init__(self, name, surname, birth, gender, ranking):
        """Init Player class."""
        self.name = name
        self.surname = surname
        self.birth_date = birth
        self.gender = gender
        self.ranking = ranking

        self.player_index = name + surname
        Player.get_all[self.player_index] = self

    def return_serialized_player(self):
        """(Put description here)."""
        return {
            "name": self.name,
            "surname": self.surname,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "ranking": self.ranking,
        }

    @staticmethod
    def save_tinyDB():
        """(Put description here)."""
        db = TinyDB("db.json")
        players_table = db.table("players")
        players_table.truncate()

        serialized_players = Player.get_serialized_players()
        players_table.insert_multiple(serialized_players)

    @staticmethod
    def get_serialized_players():
        """(Put description here)."""
        serialized_players = []
        for player in Player.get_all.values():
            serialized_players.append(player.return_serialized_player())

        return serialized_players

    @staticmethod
    def load_fromtinyDB():
        """(Put description here)."""
        db = TinyDB("db.json")
        players_table = db.table("players")

        serialized_players = players_table.all()

        for serialized_player in serialized_players:
            name = serialized_player["name"]
            surname = serialized_player["surname"]
            birth = serialized_player["birth_date"]
            gender = serialized_player["gender"]
            ranking = serialized_player["ranking"]

            Player(name, surname, birth, gender, ranking)
