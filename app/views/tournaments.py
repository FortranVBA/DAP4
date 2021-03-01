"""Project OC DAP 4 file with tournament viewer."""

from app.models.tournament import Tournament

from app.config import CommandField


class TournamentMenuViewer:
    """Project tournament viewer class."""

    def __init__(self):
        """Init tournament viewer class."""
        self.warning = ""

    def display(self):
        """Display the view and the command list."""
        self.display_warning()

        print("The list of tournament is the following :")
        for tournament in Tournament.get_all:
            print(f" - {tournament}")
        print(" ")
        print("Command list :")
        print(" - " + CommandField.NEW + " to create a new tournament")
        number = 1
        for tournament in Tournament.get_all:
            print(f" - {number}{CommandField.EDIT_TOURNAMENT} to edit {tournament}")
            number += 1
        print(
            " - " + CommandField.SAVE_TOURNAMENTS + " to save tournaments to database"
        )
        print(
            " - " + CommandField.LOAD_TOURNAMENTS + " to load tournaments from database"
        )
        print(" - " + CommandField.BACK + " to go back to main menu")
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
