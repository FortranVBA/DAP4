"""Project OC DAP 4 file with tournament related class."""

from app.views.edit_turn import EditTurnViewer

from app.config import CommandField
from app.config import ViewName


class EditTurnController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.selected_turn = ""
        self.match_number = 0
        self.tournament_name = ""

        self.command_names = {}
        self.command_names[CommandField.exit_c] = self.exit_application
        self.command_names[CommandField.back_c] = self.goto_turns_menu
        self.command_names[CommandField.match_result_c] = self.enter_score

        self.arguments_needed = {}
        self.arguments_needed[CommandField.exit_c] = self.return_no_argument
        self.arguments_needed[CommandField.back_c] = self.return_arguments_turns_menu
        self.arguments_needed[
            CommandField.match_result_c
        ] = self.return_arguments_enter_score

        self.viewer = EditTurnViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display()

    def set_selected_turn(
        self, name, tournament_name, match_description, match_results
    ):
        """(Put description here)."""
        self.selected_turn = name
        self.match_number = len(match_description)
        self.tournament_name = tournament_name

        self.viewer.set_selected_turn(
            name, tournament_name, match_description, match_results
        )

    def get_arguments(self, command):
        """(Put description here)."""
        if command in self.arguments_needed:
            return self.arguments_needed[command]()
        else:
            for number in range(1, self.match_number + 1):
                if command == str(number) + CommandField.match_result_c:
                    return self.arguments_needed[CommandField.match_result_c](number)

            return self.arguments_needed[CommandField.unknown_c]()

    def exe_command(self, command, arguments):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command](arguments)
        else:
            for number in range(1, self.match_number + 1):
                if command == str(number) + CommandField.match_result_c:
                    return self.command_names[CommandField.match_result_c](arguments)

            return self.command_names[CommandField.unknown_c](arguments)

    def exit_application(self, arguments):
        """(Put description here)."""
        return True

    def print_unknown_command(self, arguments):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False

    def return_no_argument(self):
        """(Put description here)."""
        return []

    def return_arguments_turns_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        return arguments

    def goto_turns_menu(self, arguments):
        """(Put description here)."""
        current_view = arguments[0].current_view

        current_view = ViewName.view_turns

        arguments[0].current_view = current_view

        self.viewer.warning = ""

        return False

    def return_arguments_enter_score(self, number_match):
        """(Put description here)."""
        arguments = []
        arguments.append("match" + str(number_match - 1))
        return arguments

    def enter_score(self, arguments):
        """(Put description here)."""
        match = arguments[0]

        score_player_1 = input(f"Enter score player {match.opponents[0]} : ")
        score_player_2 = input(f"Enter score player {match.opponents[1]} : ")
        match.update_result(score_player_1, score_player_2)

        arguments[0] = match

        self.viewer.update_score(match)

        return False
