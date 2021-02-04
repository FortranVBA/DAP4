"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class TurnsViewer:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        pass

    @staticmethod
    def display(tournament):
        """(Put description here)."""
        print(f"You are editing tournament {tournament.name}")
        print("List of turn :")
        for turn in tournament.turns:
            print(f" -  {turn.name}")
        print(" ")
        print("Command list :")
        number = 1
        for turn in tournament.turns:
            print(f" - {number}{CommandField.edit_turn_c} to edit {turn.name}")
            number += 1
        print(" - " + CommandField.back_c + " to go back to main menu")
        print(" - " + CommandField.exit_c + " to quit application")
