"""Project OC DAP 4 file with tournament related class."""

from app.models.player import Player

from app.views.players import PlayersViewer

from app.config import CommandField
from app.config import ViewName


class PlayersController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.current_view = ViewName.PLAYERS
        self.sub_controller = None

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
        if self.current_view == ViewName.PLAYERS:
            self.viewer.display()
        else:
            self.sub_controller.display()

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
        self.current_view = ViewName.MAIN

        self.viewer.warning = ""

        return False

    def save_database(self):
        """(Put description here)."""
        Player.save_tinyDB()

        self.viewer.warning = ""

        return False

    def load_database(self):
        """(Put description here)."""
        Player.load_fromtinyDB()

        self.viewer.warning = ""

        return False

    def print_unknown_command(self, arguments):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False
