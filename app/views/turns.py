"""Project OC DAP 4 file with turns viewer."""

from app.config import CommandField


class TurnsViewer:
    """Project turns viewer class."""

    def __init__(self):
        """Init turns viewer class."""
        self.warning = ""

    def display(self, tournament):
        """Display the view and the command list."""
        self.display_warning(tournament)

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
        print(" - " + CommandField.MATCHES + " to list all matches")
        print(" - " + CommandField.BACK + " to go back to tournament")
        print(" - " + CommandField.EXIT + " to quit application")

    def get_warning(self, tournament):
        """Return the current warning message or the requested list."""
        if self.warning == "command unknown":
            print("Warning : this command is not valid")
            print(" ")

        elif self.warning == "matches":
            for turn in tournament.turns.values():
                for match in turn.matches:
                    print(f" -  {match.opponents}  {match.result}")

        elif self.warning == "results missing":
            print("Warning : Results are missing in previous turn")
            print("New turn creation has been cancelled.")
            print(" ")

        elif self.warning == "max turn":
            print("Warning : Tournanent number of turns has been reached.")
            print("New turn creation has been cancelled.")
            print(" ")

        else:
            print("Warning : unknown error occured")

    def display_warning(self, tournament):
        """Display additional warnings or information."""
        print(" ")
        print(" ")
        if not self.warning == "":
            self.get_warning(tournament)
