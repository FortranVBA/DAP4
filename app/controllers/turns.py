"""Project OC DAP 4 file with the turns controller."""

from app.commands.navigation import GotoEditTurnMenu
from app.commands.tournament import CreateNextTurn
from app.commands.application import PrintUnknownCommand
from app.commands.tournament import ListMatchesCommand
from app.commands.application import ExitApplication
from app.commands.navigation import GoBackMenu

from app.views.turns import TurnsViewer


class TurnsController:
    """Project turns controller class."""

    def __init__(self, tournament):
        """Init turns controller class."""
        self._app = None
        self.viewer = TurnsViewer()

        self.tournament = tournament

        self.command_names = []

    def display(self):
        """Display the controller view."""
        self.viewer.display(self.tournament)

    def get_command(self):
        """Get the user input and convert it to a command instance."""
        command_input = input("Enter your command: ")

        # The 1st command in list must always be the PrintUnknownCommand, which is used
        # as default command.
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
