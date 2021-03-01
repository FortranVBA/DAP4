"""Project OC DAP 4 file with the tournament controller."""

from app.commands.tournament import LoadTournamentDatabase
from app.commands.tournament import SaveTournamentDatabase
from app.commands.navigation import GotoEditTournament
from app.commands.application import PrintUnknownCommand
from app.commands.tournament import CreateTournament
from app.commands.application import ExitApplication
from app.commands.navigation import GoBackMenu

from app.views.tournaments import TournamentMenuViewer


class TournamentMenuController:
    """Project tournament controller class."""

    def __init__(self):
        """Init tournament controller class."""
        self._app = None
        self.viewer = TournamentMenuViewer()

        self.command_names = []

    def display(self):
        """Display the controller view."""
        self.viewer.display()

    def get_command(self):
        """Get the user input and convert it to a command instance."""
        command_input = input("Enter your command: ")

        # The 1st command in list must always be the PrintUnknownCommand, which is used
        # as default command.
        self.command_names = [
            PrintUnknownCommand(self.viewer),
            ExitApplication(),
            CreateTournament(self._app, self.viewer),
            GoBackMenu(self._app, self.viewer, "main", None),
            GotoEditTournament(self._app, self.viewer),
            SaveTournamentDatabase(self.viewer),
            LoadTournamentDatabase(self.viewer),
        ]

        for command in self.command_names:
            if command.is_valid(command_input):
                self.command = command
