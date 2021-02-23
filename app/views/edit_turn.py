"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class EditTurnViewer:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.warning = ""

    def display(self, tournament, turn):
        """(Put description here)."""
        self.display_warning()

        print(f"Editing turn {turn.name} from tournament {tournament.name}")
        print(f"Time begin: {turn.time_begin}")
        print(f"Time end: {turn.time_end}")
        print("Matches list :")
        for match in turn.matches:
            print(f" -  {match.opponents}  {match.result}")
        print(" ")
        print("Command list :")
        number = 1
        for match in turn.matches:
            if len(match.opponents) == 2:
                print(
                    f" - {number}{CommandField.MATCH_RESULT} "
                    + f"to edit match results of {match.opponents}"
                )
                number += 1
        print(" - " + CommandField.BACK + " to go back to turns menu")
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
