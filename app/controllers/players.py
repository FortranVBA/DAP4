"""Project OC DAP 4 file with tournament related class."""

from app.commands.application import PrintUnknownCommand
from app.commands.player import LoadPlayerDatabase
from app.commands.player import SavePlayerDatabase
from app.commands.navigation import GoBackMenu
from app.commands.navigation import GotoEditPlayer
from app.commands.player import ListPlayersAlphabeticalCommand
from app.commands.player import ListPlayersRankingCommand
from app.commands.application import ExitApplication

from app.views.players import PlayersViewer


class PlayersController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self._app = None
        self.viewer = PlayersViewer()

        self.command_names = []

    def get_command(self):
        """(Put description here)."""
        command_input = input("Enter your command: ")

        self.command_names = [
            PrintUnknownCommand(self.viewer),
            ExitApplication(),
            GoBackMenu(self._app, self.viewer, "main", None),
            GotoEditPlayer(self._app, self.viewer, None),
            SavePlayerDatabase(self.viewer),
            LoadPlayerDatabase(self.viewer),
            ListPlayersAlphabeticalCommand(self.viewer),
            ListPlayersRankingCommand(self.viewer),
        ]

        for command in self.command_names:
            if command.is_valid(command_input):
                self.command = command

    def display(self):
        """(Put description here)."""
        self.viewer.display()
