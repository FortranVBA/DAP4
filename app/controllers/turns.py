"""Project OC DAP 4 file with tournament related class."""

from app.controllers.edit_turn import EditTurnController

from app.views.turns import TurnsViewer

from app.config import CommandField
from app.config import ViewName


class TurnsController:
    """Project application class."""

    def __init__(self, tournament):
        """Init Application class."""
        self.current_view = ViewName.TURNS
        self.sub_controller = None

        self.tournament = tournament

        self.command_names = {
            CommandField.CREATE_NEXT_TURN: self.create_next_turn,
            CommandField.EXIT: self.exit_application,
            CommandField.BACK: self.goto_edit_tournament,
            CommandField.EDIT_TURN: self.goto_edit_turn_menu,
            CommandField.UNKNOWN: self.print_unknown_command,
        }

        self.viewer = TurnsViewer()

    def display(self):
        """(Put description here)."""
        if self.current_view == ViewName.TURNS:
            self.viewer.display(self.tournament)
        else:
            self.sub_controller.display()

    def exe_command(self, command):
        """(Put description here)."""
        if self.current_view == ViewName.TURNS:
            if command in self.command_names:
                return self.command_names[command]()
            else:
                number = 1
                for turn in self.tournament.turns.values():
                    if command == str(number) + CommandField.EDIT_TURN:
                        return self.command_names[CommandField.EDIT_TURN](turn)
                    number += 1

                return self.command_names[CommandField.UNKNOWN]()
        else:
            is_exit = self.sub_controller.exe_command(command)
            if self.sub_controller.current_view == ViewName.TURNS:
                self.current_view = ViewName.TURNS
                self.sub_controller = None
            return is_exit

    def exit_application(self):
        """(Put description here)."""
        return True

    def goto_edit_tournament(self):
        """(Put description here)."""
        self.current_view = ViewName.EDIT_TOURNAMENT

        self.viewer.warning = ""

        return False

    def print_unknown_command(self):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False

    def goto_edit_turn_menu(self, turn):
        """(Put description here)."""
        self.sub_controller = EditTurnController(self.tournament, turn, False)

        self.current_view = ViewName.EDIT_TURN

        self.viewer.warning = ""

        return False

    def create_next_turn(self):
        """(Put description here)."""
        self.sub_controller = EditTurnController(self.tournament, None, True)

        self.current_view = ViewName.EDIT_TURN

        self.viewer.warning = ""

        return False
