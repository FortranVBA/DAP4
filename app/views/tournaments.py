"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class TournamentMenuViewer:
    """Main viewer to be handled by application."""

    def __init__(self):
        """(Put description here)."""
        pass

    @staticmethod
    def display(tournament_list):
        """(Put description here)."""
        print("The list of tournament is the following :")
        for tournament in tournament_list.values():
            print(f" - {tournament.name}")
        print(" ")
        print("Command list :")
        print(" - " + CommandField.back_c + " to go back to main menu")
        print(" - " + CommandField.exit_c + " to quit application")
