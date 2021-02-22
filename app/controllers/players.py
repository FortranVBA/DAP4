"""Project OC DAP 4 file with tournament related class."""

from app.controllers.commands import PrintUnknownCommand
from app.controllers.commands import LoadPlayerDatabase
from app.controllers.commands import SavePlayerDatabase
from app.controllers.commands import GotoMainMenu

from app.views.players import PlayersViewer

from app.config import CommandField


class PlayersController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self._app = None

        self.command_names = {
            CommandField.EXIT: self.exit_application,
            CommandField.BACK: self.goto_main_menu,
            CommandField.UNKNOWN: self.print_unknown_command,
            CommandField.SAVE_PLAYERS: self.save_database,
            CommandField.LOAD_PLAYERS: self.load_database,
        }

        self.viewer = PlayersViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display()

    def exe_command(self, command):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command]()
        else:
            return self.command_names[CommandField.UNKNOWN]()

    def exit_application(self):
        """(Put description here)."""
        return True

    def goto_main_menu(self):
        """(Put description here)."""
        return GotoMainMenu(self._app, self.viewer).exe_command()

    def save_database(self):
        """(Put description here)."""
        return SavePlayerDatabase(self.viewer).exe_command()

    def load_database(self):
        """(Put description here)."""
        return LoadPlayerDatabase(self.viewer).exe_command()

    def print_unknown_command(self, arguments):
        """(Put description here)."""
        return PrintUnknownCommand(self.viewer).exe_command()
