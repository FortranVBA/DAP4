"""Project OC DAP 4 file with tournament related class."""

from app.models.player import Player

from app.config import CommandField


class TournamentRankingViewer:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.warning = ""

    def display(self, tournament):
        """(Put description here)."""
        self.display_warning()

        print(f"You are editing tournament {tournament.name}")
        print("List of players :")
        for player, score in tournament.get_player_scores().items():
            print(f" -  {player} - {score}")
        print(" ")
        print("Command list :")
        number = 1
        for player in Player.get_all:
            print(f" - {number}{CommandField.EDIT_PLAYER} to edit {player}")
            number += 1
        print(" - " + CommandField.ADD_PLAYER + " to add player")
        print(" - " + CommandField.GENERATE_PLAYERS + " to generate 8 players")
        print(" - " + CommandField.BACK + " to go back to tournament")
        print(" - " + CommandField.EXIT + " to quit application")

    def get_warning(self):
        """(Put description here)."""
        if self.warning == "command unknown":
            return "Warning : this command is not valid"
        else:
            return "Warning : unknown error occured"

    def display_warning(self):
        """(Put description here)."""
        print(" ")
        print(" ")
        if not self.warning == "":
            print(self.get_warning())
