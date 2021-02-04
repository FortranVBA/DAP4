"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class MainMenuViewer:
    """Main viewer to be handled by application."""

    def __init__(self):
        """(Put description here)."""
        pass

    @staticmethod
    def display():
        """(Put description here)."""
        print("Main menu")
        print(" ")
        print("Command list :")
        print(" - " + CommandField.new_c + " to create a new tournament")
        print(" - " + CommandField.tournaments_c + " to see the list of tournaments")
        print(" - " + CommandField.print_c + " to generate reports")
        print(" - " + CommandField.exit_c + " to quit application")
