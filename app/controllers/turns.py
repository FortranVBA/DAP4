"""Project OC DAP 4 file with tournament related class."""

from app.commands.navigation import GotoEditTurnMenu
from app.commands.tournament import CreateNextTurn
from app.commands.application import PrintUnknownCommand
from app.commands.tournament import ListMatchesCommand
from app.commands.application import ExitApplication
from app.commands.navigation import GoBackMenu

from app.views.turns import TurnsViewer


class TurnsController:
    """Project application class."""

    def __init__(self, tournament):
        """Init Application class."""
        self._app = None
        self.viewer = TurnsViewer()

        self.tournament = tournament

        self.command_names = []

    def get_command(self):
        """(Put description here)."""
        command_input = input("Enter your command: ")

        self.command_names = [
            PrintUnknownCommand(self.viewer),
            ExitApplication(),
            CreateNextTurn(self._app, self.viewer, self.tournament),
            GoBackMenu(self._app, self.viewer, "edit_tournament", self.tournament),
            GotoEditTurnMenu(self._app, self.viewer, self.tournament),
            ListMatchesCommand(self.viewer),
        ]

        for command in self.command_names:
            if command.is_valid(command_input):
                self.command = command

    def display(self):
        """(Put description here)."""
        self.viewer.display(self.tournament)
