"""Project OC DAP 4 file with the players controller."""

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
    """Project players controller class."""

    def __init__(self):
        """Init players controller class."""
        self._app = None
        self.viewer = PlayersViewer()

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
