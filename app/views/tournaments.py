"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class TournamentMenuViewer:
    """Main viewer to be handled by application."""

    def __init__(self):
        """(Put description here)."""
        self.warning = ""
        self.tournaments_names = []

    def display(self):
        """(Put description here)."""
        self.display_warning()

        print("The list of tournament is the following :")
        for tournament in self.tournaments_names:
            print(f" - {tournament}")
        print(" ")
        print("Command list :")
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

    def set_tournament_names(self, tournament_names):
        """(Put description here)."""
        self.tournaments_names = tournament_names[:]
