"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class PlayersViewer:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.warning = ""
        self.player_names = []

    def display(self):
        """(Put description here)."""
        self.display_warning()

        print("The list of players is the following :")
        for player in self.player_names:
            print(f" - {player}")
        print(" ")
        print("Command list :")
        print(" - " + CommandField.save_players_c + " to save players list")
        print(" - " + CommandField.back_c + " to go back to main menu")
        print(" - " + CommandField.exit_c + " to quit application")

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

    def set_player_names(self, player_names):
        """(Put description here)."""
        self.player_names = player_names[:]
