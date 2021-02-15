"""Project OC DAP 4 file with tournament related class."""

from app.models.swiss import SwissSystem
from app.models.turn import Turn
from app.models.player import Player


class Tournament:
    """Tournament characteristics to be handled by application."""

    get_all: dict = {}

    def __init__(self, name):
        """Init Tournament class."""
        self.name = name
        self.location = "Unknown"
        self.date = "Unknown"
        self.turn_number = 4
        self.turns = {}
        self.players_index = []
        self.time_control = ""
        self.description = ""

        Tournament.get_all[self.name] = self

    def get_next_turn(self, name):
        """(Put description here)."""
        previous_matchs = []
        player_rank = {}

        # previous_matchs = [["p1", "p4"], ["p8", "p6"], ["p3", "p5"], ["p7", "p2"]]

        # player_rank["p1"] = 5
        # player_rank["p2"] = 99
        # player_rank["p3"] = 54
        # player_rank["p4"] = 7
        # player_rank["p5"] = 60
        # player_rank["p6"] = 42
        # player_rank["p7"] = 97
        # player_rank["p8"] = 12

        for player in self.players_index:
            player_rank[player] = Player.get_all[player].ranking

        self.turns[name] = Turn(
            name, SwissSystem.get_next_turn(previous_matchs, player_rank)
        )

    def get_previous_match(self):
        """(Put description here)."""
        result = []
        for turn in self.turns:
            for match in turn.matches:
                pass

        return result
