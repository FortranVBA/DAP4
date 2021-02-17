"""Project OC DAP 4 file with tournament related class."""

from app.models.player import Player

from app.config import CommandField


class PlayersViewer:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.warning = ""

    def display(self):
        """(Put description here)."""
        self.display_warning()

        print("The list of players is the following :")
        for player in Player.get_all:
            print(f" - {player}")
        print(" ")
        print("Command list :")
        print(" - " + CommandField.SAVE_PLAYERS + " to save players to database")
        print(" - " + CommandField.LOAD_PLAYERS + " to load players to database")
        print(" - " + CommandField.BACK + " to go back to main menu")
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
