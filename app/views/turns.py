"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class TurnsViewer:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.warning = ""
        self.tournament_name = ""
        self.turn_names = []

    def display(self):
        """(Put description here)."""
        self.display_warning()

        print(f"You are editing tournament {self.tournament_name}")
        print("List of turn :")
        for turn in self.turn_names:
            print(f" -  {turn}")
        print(" ")
        print("Command list :")
        number = 1
        for turn in self.turn_names:
            print(f" - {number}{CommandField.edit_turn_c} to edit {turn}")
            number += 1
        print(" - " + CommandField.back_c + " to go back to tournament")
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

    def set_viewer(self, tournament_name, turn_names):
        """(Put description here)."""
        self.tournament_name = tournament_name
        self.turn_names = turn_names[:]
