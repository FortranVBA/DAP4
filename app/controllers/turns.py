"""Project OC DAP 4 file with tournament related class."""

from app.views.turns import TurnsViewer

from app.config import CommandField
from app.config import ViewName


class TurnsController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.turn_number = 0

        self.command_names = {}
        self.command_names[CommandField.exit_c] = self.exit_application
        self.command_names[CommandField.back_c] = self.goto_edit_tournament
        self.command_names[CommandField.edit_turn_c] = self.goto_edit_turn_menu

        self.arguments_needed = {}
        self.arguments_needed[CommandField.exit_c] = self.return_no_argument
        self.arguments_needed[
            CommandField.back_c
        ] = self.return_arguments_edit_tournament
        self.arguments_needed[
            CommandField.edit_turn_c
        ] = self.return_arguments_edit_turn

        self.viewer = TurnsViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display()

    def get_arguments(self, command):
        """(Put description here)."""
        if command in self.arguments_needed:
            return self.arguments_needed[command]()
        else:
            for number in range(1, self.turn_number + 1):
                if command == str(number) + CommandField.edit_turn_c:
                    return self.arguments_needed[CommandField.edit_turn_c](number)

            return self.arguments_needed[CommandField.unknown_c]()

    def exe_command(self, command, arguments):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command](arguments)
        else:
            for number in range(1, self.turn_number + 1):
                if command == str(number) + CommandField.edit_turn_c:
                    return self.command_names[CommandField.edit_turn_c](arguments)

            return self.command_names[CommandField.unknown_c](arguments)

    def return_no_argument(self):
        """(Put description here)."""
        return []

    def exit_application(self, arguments):
        """(Put description here)."""
        return True

    def return_arguments_edit_tournament(self):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        arguments.append("edit_tournament_controller")
        arguments.append("active_tournament")
        return arguments

    def goto_edit_tournament(self, arguments):
        """(Put description here)."""
        current_view = arguments[0].current_view
        edit_tournament_controller = arguments[1]
        active_tournament = arguments[2]

        current_view = ViewName.view_edit_tournament
        edit_tournament_controller.set_selected_tournament(active_tournament)

        arguments[0].current_view = current_view
        arguments[1] = edit_tournament_controller
        arguments[2] = active_tournament

        self.viewer.warning = ""

        return False

    def print_unknown_command(self, arguments):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False

    def set_viewer(self, tournament):
        """(Put description here)."""
        self.viewer.set_viewer(tournament.name, list(tournament.turns.keys()))
        self.turn_number = len(tournament.turns)

    def return_arguments_edit_turn(self, number_turn):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        arguments.append("edit_turn_controller")
        arguments.append("active_tournament")
        arguments.append("turn" + str(number_turn - 1))
        return arguments

    def goto_edit_turn_menu(self, arguments):
        """(Put description here)."""
        current_view = arguments[0].current_view
        edit_turn_controller = arguments[1]
        active_tournament = arguments[2]
        turn = arguments[3]

        current_view = ViewName.view_edit_turn

        edit_turn_controller.set_selected_turn(
            active_tournament.name,
            turn,
        )

        arguments[0].current_view = current_view
        arguments[1] = edit_turn_controller
        arguments[2] = active_tournament
        arguments[3] = turn

        self.viewer.warning = ""

        return False
