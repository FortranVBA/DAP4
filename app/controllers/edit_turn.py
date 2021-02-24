"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import PrintUnknownCommand
from app.controllers.commands import EnterScore
from app.controllers.commands import GotoTurnsMenu
from app.controllers.commands import CompleteEndTurn

from app.views.edit_turn import EditTurnViewer

from app.config import CommandField


class EditTurnController:
    """Project application class."""

    def __init__(self, tournament, turn, is_new):
        """Init Application class."""
        self._app = None
        self.tournament = tournament

        if is_new:
            already_exists = True
            while already_exists:
                name_new = input("Enter your turn name : ")
                if name_new in tournament.turns:
                    print("This name is already taken, please enter another one.")
                else:
                    already_exists = False

            self.tournament.get_next_turn(name_new)
            self.turn = self.tournament.turns[name_new]
        else:
            self.turn = turn

        self.command_names = {
            CommandField.EXIT: self.exit_application,
            CommandField.BACK: self.goto_turns_menu,
            CommandField.MATCH_RESULT: self.enter_score,
            CommandField.UNKNOWN: self.print_unknown_command,
        }

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
                if len(match.opponents) == 2:
                    if command == str(number) + CommandField.MATCH_RESULT:
                        return self.command_names[CommandField.MATCH_RESULT](match)
                    number += 1

            return self.command_names[CommandField.UNKNOWN]()

    def exit_application(self):
        """(Put description here)."""
        return True

    def print_unknown_command(self):
        """(Put description here)."""
        return PrintUnknownCommand(self.viewer).exe_command()

    def goto_turns_menu(self):
        """(Put description here)."""
        return GotoTurnsMenu(self._app, self.viewer, self.tournament).exe_command()

    def enter_score(self, match):
        """(Put description here)."""
        first_command = EnterScore(match).exe_command()
        second_command = CompleteEndTurn(self.turn).exe_command()

        return first_command and second_command
