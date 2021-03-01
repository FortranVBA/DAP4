"""Project OC DAP 4 file with tournament related class."""

from app.commands.tournament import LoadTournamentDatabase
from app.commands.tournament import SaveTournamentDatabase
from app.commands.navigation import GotoEditTournament
from app.commands.application import PrintUnknownCommand
from app.commands.tournament import CreateTournament
from app.commands.application import ExitApplication
from app.commands.navigation import GoBackMenu

from app.views.tournaments import TournamentMenuViewer


class TournamentMenuController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self._app = None
        self.viewer = TournamentMenuViewer()

        self.command_names = []

    def get_command(self):
        """(Put description here)."""
        command_input = input("Enter your command: ")

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

    def display(self):
        """(Put description here)."""
        self.viewer.display()
