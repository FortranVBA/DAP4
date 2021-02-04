"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class PrintMenuViewer:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        pass

    @staticmethod
    def display():
        """(Put description here)."""
        print("What report do you want ?")
        print(" ")
        print("Command list :")
        print(" - " + CommandField.back_c + " to go back to main menu")
        print(" - " + CommandField.exit_c + " to quit application")
