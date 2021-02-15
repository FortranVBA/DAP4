"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class MainMenuViewer:
    """Main viewer to be handled by application."""

    def __init__(self):
        """(Put description here)."""
        self.warning = ""

    def display(self):
        """(Put description here)."""
        self.display_warning()

        print("Main menu")
        print(" ")
        print("Command list :")
        print(" - " + CommandField.tournaments_c + " to see the list of tournaments")
        print(" - " + CommandField.players_c + " to see the list of players")
        print(" - " + CommandField.print_c + " to generate reports")
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
