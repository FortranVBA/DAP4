"""Project OC DAP 4 file with tournament related class."""

from app.views.edit_turn import EditTurnViewer

from app.config import CommandField
from app.config import ViewName

# from app.models.turn import Turn


class EditTurnController:
    """Project application class."""

    def __init__(self, tournament, turn, is_new):
        """Init Application class."""
        self.current_view = ViewName.view_edit_turn
        self.tournament = tournament

        if is_new:
            name_new = input("Enter turn name : ")
            self.tournament.get_next_turn(name_new)
            self.turn = self.tournament.turns[name_new]
        else:
            self.turn = turn

        self.command_names = {}
        self.command_names[CommandField.exit_c] = self.exit_application
        self.command_names[CommandField.back_c] = self.goto_turns_menu
        self.command_names[CommandField.match_result_c] = self.enter_score

        self.viewer = EditTurnViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display(self.tournament, self.turn)

    def exe_command(self, command):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command]()
        else:
            number = 1
            for match in self.turn.matches:
                if command == str(number) + CommandField.match_result_c:
                    return self.command_names[CommandField.match_result_c](match)
                number += 1

            return self.command_names[CommandField.unknown_c]()

    def exit_application(self):
        """(Put description here)."""
        return True

    def print_unknown_command(self):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False

    def return_arguments_turns_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        arguments.append("turns_controller")
        arguments.append("active_tournament")
        return arguments

    def goto_turns_menu(self, arguments):
        """(Put description here)."""
        current_view = arguments[0].current_view
        turns_controller = arguments[1]
        active_tournament = arguments[2]

        current_view = ViewName.view_turns
        turns_controller.set_viewer(active_tournament)

        arguments[0].current_view = current_view
        arguments[1] = turns_controller
        arguments[2] = active_tournament

        self.viewer.warning = ""

        return False

    def return_arguments_enter_score(self, number_match):
        """(Put description here)."""
        arguments = []
        arguments.append("match" + str(number_match - 1))
        return arguments

    def enter_score(self, match):
        """(Put description here)."""
        score_player_1 = input(f"Enter score player {match.opponents[0]} : ")
        score_player_2 = input(f"Enter score player {match.opponents[1]} : ")
        match.update_result(score_player_1, score_player_2)

        return False
