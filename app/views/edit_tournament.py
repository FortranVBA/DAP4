"""Project OC DAP 4 file with the edit_tournament viewer."""

from app.config import CommandField


class EditTournamentViewer:
    """Project edit_tournament viewer class."""

    def __init__(self):
        """Init edit_tournament viewer class."""
        self.warning = ""

    def display(self, tournament):
        """Display the view and the command list."""
        self.display_warning()

        print(f"You are editing tournament {tournament.name}")
        print(f" Location :  {tournament.location}")
        print(f" Date  {tournament.date}")
        print(f" Number of turns  {tournament.turn_number}")
        print(f" Number of rounds created : {len(tournament.turns)}")
        print(f" Number of players : {len(tournament.players_index)}")
        print(f" Time control : {tournament.time_control}")
        print(f" Description  : {tournament.description}")
        print(" ")
        print("Command list :")
        print(" - " + CommandField.TOURNAMENT_LOCATION + " to edit location")
        print(" - " + CommandField.TOURNAMENT_DATE + " to edit date")
        print(" - " + CommandField.TOURNAMENT_TURN_NUMBER + " to change turn number")
        print(" - " + CommandField.TOURNAMENT_TIME + " to change time control")
        print(" - " + CommandField.TOURNAMENT_DESCRIPTION + " to change description")
        print(" - " + CommandField.RANKING + " to edit players and see ranking")
        print(" - " + CommandField.TURNS + " to view and edit turns")
        print(" - " + CommandField.BACK + " to go back to tournament menu")
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
