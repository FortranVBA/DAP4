"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import GotoEditTurnMenu
from app.controllers.commands import GotoEditTournament
from app.controllers.commands import CreateNextTurn
from app.controllers.commands import PrintUnknownCommand

from app.views.turns import TurnsViewer

from app.config import CommandField


class TurnsController:
    """Project application class."""

    def __init__(self, tournament):
        """Init Application class."""
        self._app = None
        self.viewer = TurnsViewer()

        self.tournament = tournament

        self.command_names = {
            CommandField.CREATE_NEXT_TURN: self.create_next_turn,
            CommandField.EXIT: self.exit_application,
            CommandField.BACK: self.goto_edit_tournament,
            CommandField.EDIT_TURN: self.goto_edit_turn_menu,
            CommandField.UNKNOWN: self.print_unknown_command,
        }

    def display(self):
        """(Put description here)."""
        self.viewer.display(self.tournament)

    def exe_command(self, command):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command]()
        else:
            number = 1
            for turn in self.tournament.turns.values():
                if command == str(number) + CommandField.EDIT_TURN:
                    return self.command_names[CommandField.EDIT_TURN](turn)
                number += 1

            return self.command_names[CommandField.UNKNOWN]()

    def exit_application(self):
        """(Put description here)."""
        return True

    def goto_edit_tournament(self):
        """(Put description here)."""
        return GotoEditTournament(self._app, self.viewer, self.tournament).exe_command()

    def print_unknown_command(self):
        """(Put description here)."""
        return PrintUnknownCommand(self.viewer).exe_command()

    def goto_edit_turn_menu(self, turn):
        """(Put description here)."""
        return GotoEditTurnMenu(
            self._app, self.viewer, self.tournament, turn
        ).exe_command()

    def create_next_turn(self):
        """(Put description here)."""
        return CreateNextTurn(self._app, self.viewer, self.tournament).exe_command()
