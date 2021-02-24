"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class EditTournamentViewer:
    """Project application class."""

    def __init__(self):
        """(Put description here)."""
        self.warning = ""

    def display(self, tournament):
        """(Put description here)."""
        self.display_warning()

        print(f"You are editing tournament {tournament.name}")
        print(f" Location :  {tournament.location}")
        print(f" Date  {tournament.date}")
        print(f" Number of turns  {tournament.turn_number}")
        print(f"Number of rounds created : {len(tournament.turns)}")
        print(f"Number of players : {len(tournament.players_index)}")
        print(f" Time control {tournament.time_control}")
        print(f"Description  {tournament.description}")
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
