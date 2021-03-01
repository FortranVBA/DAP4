"""Project OC DAP 4 file with the edit_player viewer."""

from app.config import CommandField


class EditPlayerViewer:
    """Project edit_player viewer class."""

    def __init__(self):
        """Init edit_player viewer class."""
        self.warning = ""

    def display(self, player):
        """Display the view and the command list."""
        self.display_warning()

        print(f"Editing player ID {player.player_index}")
        print(f" - Name : {player.name}")
        print(f" - Surname : {player.surname}")
        print(f" - Birth date : {player.birth_date}")
        print(f" - Gender : {player.gender}")
        print(f" - Ranking : {player.ranking}")
        print("Command list :")
        print(" - " + CommandField.UPDATE_RANKING + " to update player ranking")
        print(" - " + CommandField.BACK + " to go back to previous menu")
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
