"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class EditTurnViewer:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        pass

    @staticmethod
    def display(tournament, turn_selected, player_list):
        """(Put description here)."""
        print(f"You are editing turn {turn_selected} from tournament {tournament.name}")
        print("Matches list :")
        for match in tournament.turns[turn_selected].matches:
            print(f" -  {match.opponents}")
        print(" ")
        print("Command list :")
        print(" - " + CommandField.back_c + " to go back to turns menu")
        print(" - " + CommandField.exit_c + " to quit application")
