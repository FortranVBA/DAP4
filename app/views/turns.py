"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class TurnsViewer:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.warning = ""

    def display(self, tournament):
        """(Put description here)."""
        self.display_warning()

        print(f"You are editing tournament {tournament.name}")
        print("List of turn :")
        for turn in tournament.turns:
            print(f" -  {turn}")
        print(" ")
        print("Command list :")
        print(" - " + CommandField.CREATE_NEXT_TURN + " to create the next turn")
        number = 1
        for turn in tournament.turns.values():
            print(f" - {number}{CommandField.EDIT_TURN} to edit {turn.name}")
            number += 1
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
