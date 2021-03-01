"""Project OC DAP 4 file with the main_menu viewer."""

from app.config import CommandField


class MainMenuViewer:
    """Project main_menu viewer class."""

    def __init__(self):
        """Init main_menu viewer class."""
        self.warning = ""

    def display(self):
        """Display the view and the command list."""
        self.display_warning()

        print("Main menu")
        print(" ")
        print("Command list :")
        print(" - " + CommandField.TOURNAMENTS + " to see the list of tournaments")
        print(" - " + CommandField.PLAYERS + " to see the list of players")
        print(" - " + CommandField.EXIT + " to quit application")

    def get_warning(self):
        """Return the current warning message."""
        if self.warning == "command unknown":
            return "Warning : this command is not valid"
        else:
            return "Warning : unknown error occured"

    def display_warning(self):
        """Display additional warnings."""
        print(" ")
        print(" ")
        if not self.warning == "":
            print(self.get_warning())
