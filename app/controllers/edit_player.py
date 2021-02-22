"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import PrintUnknownCommand
from app.controllers.commands import GoBackMenu

from app.views.edit_player import EditPlayerViewer

from app.config import CommandField


class EditPlayerController:
    """Project application class."""

    def __init__(self, player, tournament):
        """Init Application class."""
        self._app = None
        self.player = player
        self.tournament = tournament

        self.command_names = {
            CommandField.EXIT: self.exit_application,
            CommandField.BACK: self.go_back,
            CommandField.UNKNOWN: self.print_unknown_command,
        }

        self.viewer = EditPlayerViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display(self.player)

    def exe_command(self, command):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command]()
        else:
            return self.command_names[CommandField.UNKNOWN]()

    def exit_application(self):
        """(Put description here)."""
        return True

    def print_unknown_command(self):
        """(Put description here)."""
        return PrintUnknownCommand(self.viewer).exe_command()

    def go_back(self):
        """(Put description here)."""
        return GoBackMenu(self._app, self.viewer, self.tournament).exe_command()
