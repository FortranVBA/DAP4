"""Project OC DAP 4 file with tournament related class."""

from tinydb import TinyDB

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

    def set_tournament(
        self,
        location,
        date,
        turn_number,
        turns_parameters,
        players_index,
        time_control,
        description,
    ):
        """(Put description here)."""
        self.location = location
        self.date = date
        self.turn_number = turn_number
        for turn in turns_parameters:
            self.turns[turn["name"]] = Turn(
                turn["name"],
                turn["matches_input"],
                turn["matches_result"],
                turn["time_begin"],
                turn["time_end"],
            )
        self.players_index = players_index
        self.time_control = time_control
        self.description = description

    def return_serialized_player(self):
        """(Put description here)."""
        turns_serialized = []
        for turn in self.turns.values():
            turns_serialized.append(turn.return_serialized_turn())

        return {
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "turn_number": self.turn_number,
            "turns": turns_serialized,
            "players_index": self.players_index,
            "time_control": self.time_control,
            "description": self.description,
        }

    def get_next_turn(self, name):
        """(Put description here)."""
        previous_matchs = self.get_previous_match()
        player_rank = self.get_player_rank()

        matches_input, match_result = SwissSystem.get_next_turn(
            previous_matchs, player_rank
        )

        from datetime import datetime

        self.turns[name] = Turn(
            name,
            matches_input,
            match_result,
            datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            "",
        )

    def get_previous_match(self):
        """(Put description here)."""
        result = []
        for turn in self.turns.values():
            for match in turn.matches:
                result.append(match.opponents)

        return result

    def get_player_rank(self):
        """(Put description here)."""
        results = {}

        if len(self.turns) == 0:
            for player in self.players_index:
                results[player] = Player.get_all[player].ranking

        else:
            number = 1
            for player in self.get_player_scores():
                results[player] = number
                number += 1

        return results

    def get_player_scores(self):
        """(Put description here)."""
        scores = {}

        for player in self.players_index:
            scores[player] = 0

        for turn in self.turns.values():
            for match in turn.matches:
                if not match.result == ():
                    scores[match.opponents[0]] += float(match.result[0])
                    if len(match.opponents) == 2:
                        scores[match.opponents[1]] += float(match.result[1])

        sorted_scores = dict(
            sorted(scores.items(), key=lambda item: item[1], reverse=True)
        )

        return sorted_scores

    @staticmethod
    def get_serialized_tournament():
        """(Put description here)."""
        serialized_tournament = []
        for tournament in Tournament.get_all.values():
            serialized_tournament.append(tournament.return_serialized_player())

        return serialized_tournament

    @staticmethod
    def save_tinyDB():
        """(Put description here)."""
        Player.save_tinyDB()

        db = TinyDB("db.json")
        tournaments_table = db.table("tournaments")
        tournaments_table.truncate()

        serialized_tournaments = Tournament.get_serialized_tournament()
        tournaments_table.insert_multiple(serialized_tournaments)

    @staticmethod
    def load_fromtinyDB():
        """(Put description here)."""
        Player.load_fromtinyDB()

        db = TinyDB("db.json")
        tournaments_table = db.table("tournaments")

        serialized_tournaments = tournaments_table.all()

        for serialized_tournament in serialized_tournaments:
            name = serialized_tournament["name"]
            Tournament(name)

            location = serialized_tournament["location"]
            date = serialized_tournament["date"]
            turn_number = serialized_tournament["turn_number"]
            turns_parameters = serialized_tournament["turns"]
            players_index = serialized_tournament["players_index"]
            time_control = serialized_tournament["time_control"]
            description = serialized_tournament["description"]

            Tournament.get_all[name].set_tournament(
                location,
                date,
                turn_number,
                turns_parameters,
                players_index,
                time_control,
                description,
            )
