"""Project OC DAP 4 file with the edit_player controller."""

from app.commands.application import PrintUnknownCommand
from app.commands.navigation import GoBackMenu
from app.commands.player import UpdatePlayerRanking
from app.commands.application import ExitApplication

from app.views.edit_player import EditPlayerViewer


class EditPlayerController:
    """Project edit_player controller class."""

    def __init__(self, player, tournament):
        """Init edit_player controller class."""
        self._app = None
        self.player = player
        self.tournament = tournament

        self.command_names = []

        self.viewer = EditPlayerViewer()

    def display(self):
        """Display the controller view."""
        self.viewer.display(self.player)

    def get_command(self):
        """Get the user input and convert it to a command instance."""
        command_input = input("Enter your command: ")

        # The 1st command in list must always be the PrintUnknownCommand, which is used
        # as default command.
        self.command_names = [
            PrintUnknownCommand(self.viewer),
            ExitApplication(),
            GoBackMenu(self._app, self.viewer, "", self.tournament),
            UpdatePlayerRanking(self.viewer, self.player),
        ]

        for command in self.command_names:
            if command.is_valid(command_input):
                self.command = command
