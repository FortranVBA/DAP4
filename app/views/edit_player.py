"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class EditPlayerViewer:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.warning = ""

    def display(self, player):
        """(Put description here)."""
        self.display_warning()

        print(f"Editing player ID {player.player_index}")
        print(f" - Name : {player.name}")
        print(f" - Surname : {player.surname}")
        print(f" - Birth date : {player.birth_date}")
        print(f" - Gender : {player.gender}")
        print(f" - Ranking : {player.ranking}")
        print("Command list :")
        print(" - " + CommandField.BACK + " to go back to previous menu")
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
