"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import PrintUnknownCommand
from app.controllers.commands import EnterScore
from app.controllers.commands import ExitApplication
from app.controllers.commands import GoBackMenu

from app.views.edit_turn import EditTurnViewer


class EditTurnController:
    """Project application class."""

    def __init__(self, tournament, turn, is_new):
        """Init Application class."""
        self._app = None
        self.tournament = tournament
        self.viewer = EditTurnViewer()

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

        self.command_names = []

    def get_command(self):
        """(Put description here)."""
        command_input = input("Enter your command: ")

        self.command_names = [
            PrintUnknownCommand(self.viewer),
            ExitApplication(),
            GoBackMenu(self._app, self.viewer, "turns", self.tournament),
            EnterScore(self.turn),
        ]

        for command in self.command_names:
            if command.is_valid(command_input):
                self.command = command

    def display(self):
        """(Put description here)."""
        self.viewer.display(self.tournament, self.turn)
