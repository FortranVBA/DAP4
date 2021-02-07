"""Project OC DAP 4 file with tournament related class."""

from app.config import CommandField


class EditTurnViewer:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.warning = ""
        self.turn_selected = ""
        self.tournament_name = ""
        self.match_description = []
        self.match_results = []

    def set_selected_turn(
        self, name, tournament_name, match_description, match_results
    ):
        """Init Application class."""
        self.turn_selected = name
        self.tournament_name = tournament_name
        self.match_description = match_description[:]
        self.match_results = match_results[:]

    def update_score(self, updated_match):
        """(Put description here)."""
        index_match = 0
        for match in self.match_description:
            if str(match) == str(updated_match.opponents):
                self.match_results[index_match] = updated_match.result
            index_match += 1

    def display(self):
        """(Put description here)."""
        self.display_warning()

        print(
            f"Editing turn {self.turn_selected} from tournament {self.tournament_name}"
        )
        print("Matches list :")
        for description, result in zip(self.match_description, self.match_results):
            print(f" -  {description}  {result}")
        print(" ")
        print("Command list :")
        number = 1
        for description in self.match_description:
            print(
                f" - {number}{CommandField.match_result_c} "
                + f"to edit match results of {description}"
            )
            number += 1
        print(" - " + CommandField.back_c + " to go back to turns menu")
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
