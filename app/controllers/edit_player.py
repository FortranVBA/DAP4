"""Project OC DAP 4 file with tournament related class."""

from app.commands.application import PrintUnknownCommand
from app.commands.navigation import GoBackMenu
from app.commands.player import UpdatePlayerRanking
from app.commands.application import ExitApplication

from app.views.edit_player import EditPlayerViewer


class EditPlayerController:
    """Project application class."""

    def __init__(self, player, tournament):
        """Init Application class."""
        self._app = None
        self.player = player
        self.tournament = tournament

        self.command_names = []

        self.viewer = EditPlayerViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display(self.player)

    def get_command(self):
        """(Put description here)."""
        command_input = input("Enter your command: ")

        self.command_names = [
            PrintUnknownCommand(self.viewer),
            ExitApplication(),
            GoBackMenu(self._app, self.viewer, "", self.tournament),
            UpdatePlayerRanking(self.viewer, self.player),
        ]

        for command in self.command_names:
            if command.is_valid(command_input):
                self.command = command
